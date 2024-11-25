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

    Args:
        agents: List of LLM agents to process the tasks
        filenames: List of task file paths to be processed

    Returns:
        List[dict]: Collection of processed responses from all agents
    """
    tasks = [
        agent.get_response(filename)
        for agent, filename in zip(agents, filenames)
    ]
    return await asyncio.gather(*tasks)


async def main(submission_dir: str) -> None:
    """
    Process a single student's submission directory.

    Args:
        submission_dir: Path to the student's submission directory

    Note:
        Moves processed directories to 'Done' folder upon completion
    """
    agents = initialize_agents()
    student_name = extract_student_name(submission_dir)
    
    try:
        # Process submission files
        filenames = find_task_files(submission_dir)
        responses = await gather_responses(agents, filenames)
        
        # Save results
        save_responses_json(responses, student_name)
        final_scores = calculate_final_grade(responses)
        save_scores_csv(final_scores, student_name)
        
        # Move processed submission to Done directory
        shutil.move(
            submission_dir,
            os.path.join('Done', os.path.basename(submission_dir))
        )
    
    except Exception as e:
        print(f"Error processing submission: {e}")
        save_scores_csv([], student_name)


if __name__ == "__main__":
    submission_root = "Renamed"
    submission_dirs = glob.glob(os.path.join(submission_root, '*'))
    
    # Process each submission with progress bar
    for submission_dir in tqdm(submission_dirs, desc="Processing submissions"):
        student_name = extract_student_name(submission_dir)
        print(f"Processing: {' '.join(student_name)}")
        asyncio.run(main(submission_dir=submission_dir))