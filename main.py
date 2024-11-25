"""
Main grading script for automated assessment of student submissions.
Processes multiple student directories and generates score reports.
"""

import asyncio
import glob
import os
import shutil
from typing import List

import nest_asyncio
from tqdm import tqdm

from PROMPTS.ASS03 import (
    TASK01, TASK02, TASK03,
    TASK04, TASK05, TASK06
)
from PROMPTS.PARSER import (
    parse_question_one,
    parse_question_two,
    parse_question_three,
    parse_question_four,
    parse_question_five,
    parse_question_six
)
from llm import LLM
from utils import (
    extract_student_name,
    find_task_files,
    save_responses_json,
    calculate_final_grade,
    save_scores_csv
)

# Enable nested event loops for async operations
nest_asyncio.apply()


def initialize_agents() -> List[LLM]:
    """
    Initialize LLM agents with their respective prompts and response parsers.

    Returns:
        List[LLM]: List of initialized LLM agents for each task.
    """
    return [
        LLM(prompt_template=TASK01, parser=parse_question_one),
        LLM(prompt_template=TASK02, parser=parse_question_two),
        LLM(prompt_template=TASK03, parser=parse_question_three),
        LLM(prompt_template=TASK04, parser=parse_question_four),
        LLM(prompt_template=TASK05, parser=parse_question_five),
        LLM(prompt_template=TASK06, parser=parse_question_six),
    ]


async def gather_responses(agents: List[LLM], filenames: List[str]) -> List[dict]:
    """
    Collect responses from LLM agents for each task file asynchronously.
    If a filename is None, return a zero score for that task.
    """
    tasks = []
    responses = []
    
    for task_num, (agent, filename) in enumerate(zip(agents, filenames), 1):
        if filename is None:
            # Create a zero score response for missing file
            responses.append({
                'task_number': task_num,
                'score': 0,
                'feedback': f'Task {task_num}: No file submitted',
                'error': 'Missing file',
                'final_score': 0
            })
        else:
            # Queue the task for processing
            tasks.append(agent.get_response(filename))
            # Keep track of task numbers for successful responses
            responses.append(task_num)
    
    # Process all valid files
    if tasks:
        results = await asyncio.gather(*tasks)
        
        # Replace task numbers with actual responses
        for i, result in enumerate(results):
            # Find the next task number placeholder in responses
            for j, resp in enumerate(responses):
                if isinstance(resp, int):
                    responses[j] = {**result, 'task_number': resp}
                    break
    
    return responses


async def process_submission_batch(submissions: List[str]) -> None:
    """
    Process a batch of student submissions concurrently.
    
    Args:
        submissions: List of submission directory paths to process
    """
    tasks = [main(submission) for submission in submissions]
    await asyncio.gather(*tasks)

async def main(submission_dir: str) -> None:
    """
    Process a single student's submission directory with retry logic.
    """
    if not submission_dir or not os.path.exists(submission_dir):
        print(f"Invalid submission directory: {submission_dir}")
        return

    agents = initialize_agents()
    student_name = extract_student_name(submission_dir)
    
    for attempt in range(2):  # Try twice
        try:
            filenames = find_task_files(submission_dir)
            responses = await gather_responses(agents, filenames)
            save_responses_json(responses, student_name)
            final_scores = calculate_final_grade(responses)
            save_scores_csv(final_scores, student_name)
            
            # Move processed submission
            done_path = os.path.join('Done', os.path.basename(submission_dir))
            if os.path.exists(submission_dir):
                shutil.move(submission_dir, done_path)
            print(f"✅ Successfully graded: {' '.join(student_name)}")
            break
            
        except Exception as e:
            if attempt == 0:  # First attempt failed
                print(f"First attempt failed for {student_name}: {str(e)}")
                continue
            else:  # Second attempt failed
                print(f"Error processing submission {student_name}: {str(e)}")
                save_scores_csv([], student_name)  # Save empty scores

if __name__ == "__main__":
    submission_root = "Renamed"
    submission_dirs = glob.glob(os.path.join(submission_root, '*'))
    total_batches = (len(submission_dirs) + 1) // 2  # Ceiling division
    
    # Process submissions in batches of 2 with progress bar
    batch_size = 5
    with tqdm(total=total_batches, desc="Processing batches") as pbar:
        for i in range(0, len(submission_dirs), batch_size):
            batch = submission_dirs[i:i + batch_size]
            print(f"\nBatch {i//batch_size + 1}/{total_batches}")
            for submission_dir in batch:
                student_name = extract_student_name(submission_dir)
                print(f"⏳ Queued: {' '.join(student_name)}")
            asyncio.run(process_submission_batch(batch))
            pbar.update(1)
        
    print("\n✨ Grading completed! Check the Done directory and CSV files for results.")