import asyncio
import nest_asyncio
import os
import glob
import json
import csv
from tqdm import tqdm
from utils import (
    parse_question_one,
    parse_question_two,
    parse_question_three,
    parse_question_four,
    parse_question_five
)
from llm import LLM
import re
import shutil
from PROMPTS.GRADING_PROMPT import (
    TASK01,
    TASK02,
    TASK03,
    TASK04,
    TASK05
)

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

async def main(submission_dir):
    """
    Main function to process a student's submission directory.
    """
    agents = initialize_agents()
    student_name = extract_student_name(submission_dir)
    create_graded_directory()
    create_done_directory()
    try:
        filenames = find_task_files(submission_dir)
        responses = await gather_responses(agents, filenames)
        save_responses_json(responses, student_name)
        final_scores = calculate_final_grade(responses)
        save_scores_csv(final_scores, student_name)
        shutil.move(submission_dir, os.path.join('Done', os.path.basename(submission_dir)))
    except Exception as e:
        print(f"Error processing submission: {e}")
        save_scores_csv([], student_name)

def initialize_agents():
    """
    Initialize LLM agents with their respective prompts and parsers.
    """
    return [
        LLM(prompt_template=TASK01, parser=parse_question_one),
        LLM(prompt_template=TASK02, parser=parse_question_two),
        LLM(prompt_template=TASK03, parser=parse_question_three),
        LLM(prompt_template=TASK04, parser=parse_question_four),
        LLM(prompt_template=TASK05, parser=parse_question_five)
    ]

def extract_student_name(submission_dir):
    """
    Extract the student's name from the submission directory name.
    """
    base_name = os.path.basename(submission_dir)
    parts = base_name.strip().split()
    return [parts[0], parts[1]] if len(parts) >= 2 else [base_name, ""]

def create_graded_directory():
    """
    Create the 'Graded' directory if it does not exist.
    """
    os.makedirs('Graded', exist_ok=True)

def create_done_directory():
    """
    Create the 'Done' directory if it does not exist.
    """
    os.makedirs('Done', exist_ok=True)

def find_task_files(submission_dir):
    """
    Find task files in the submission directory based on predefined patterns.
    """
    task_patterns = [
        (1, r'(?i)(task\s*0?1|assignment\d*task\s*0?1|Task\s*1)\.py$'),
        (2, r'(?i)(task\s*0?2|assignment\d*task\s*0?2|Task\s*2)\.py$'),
        (3, r'(?i)(task\s*0?3|assignment\d*task\s*0?3|Task\s*3)\.py$'),
        (4, r'(?i)(task\s*0?4|assignment\d*task\s*0?4|Task\s*4)\.py$'),
        (5, r'(?i)(task\s*0?5|assignment\d*task\s*0?5|Task\s*5)\.py$')
    ]
    filenames = []
    for _, pattern in task_patterns:
        task_file = next((os.path.join(submission_dir, f).replace('/', '\\')
                         for f in os.listdir(submission_dir) if re.match(pattern, f)), None)
        filenames.append(task_file)
    return filenames

async def gather_responses(agents, filenames):
    """
    Gather responses from LLM agents for each task file.
    """
    tasks = [agent.get_response(filename) for agent, filename in zip(agents, filenames)]
    return await asyncio.gather(*tasks)

def save_responses_json(responses, student_name):
    """
    Save the responses from LLM agents to a JSON file.
    """
    filename = f"Graded/{'_'.join(student_name)}.json"
    with open(filename, 'w') as f:
        json.dump(responses, f, indent=4)

def calculate_final_grade(responses):
    """
    Calculate the final grade based on individual task scores and their weights.
    """
    weights = [0.20, 0.10, 0.30, 0.20, 0.20]
    scores = [int(response['final_score']) for response in responses]
    weighted_final = sum(score * weight for score, weight in zip(scores, weights))
    return scores + [round(weighted_final)]

def save_scores_csv(scores, student_name):
    """
    Save the scores to a CSV file.
    """
    csv_file = 'Graded/scores.csv'
    headers = ['First Name', 'Last Name', 'Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Final Grade']
    first, last = student_name
    row = [first, last] + scores

    # Create file with headers if it doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    # Append the scores
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

if __name__ == "__main__":
    submission_root = "Submissions01"
    submission_dirs = glob.glob(os.path.join(submission_root, '*'))
    for submission_dir in tqdm(submission_dirs, desc="Processing submissions"):
        student_name = extract_student_name(submission_dir)
        print(f"Processing: {' '.join(student_name)}")
        asyncio.run(main(submission_dir=submission_dir))