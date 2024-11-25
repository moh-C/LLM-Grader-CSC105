import os
import shutil
import re
from pathlib import Path

def ensure_dir(path):
    """Safely create directory, handling cases where path exists as a file"""
    path = Path(path)
    if path.exists():
        if not path.is_dir():
            path.unlink()  # Remove if it's a file
    path.mkdir(exist_ok=True, parents=True)

def find_task_files(submission_dir):
    """
    Find task files in the submission directory based on predefined patterns.
    Matches patterns like: task01, task1, TASK 01, Task1, etc.
    """
    task_patterns = [
        (1, r'(?i)(?:task|TASK)\s*(?:0?1|one)\.py$'),
        (2, r'(?i)(?:task|TASK)\s*(?:0?2|two)\.py$'),
        (3, r'(?i)(?:task|TASK)\s*(?:0?3|three)\.py$'),
        (4, r'(?i)(?:task|TASK)\s*(?:0?4|four)\.py$'),
        (5, r'(?i)(?:task|TASK)\s*(?:0?5|five)\.py$')
    ]
    filenames = []
    submission_path = Path(submission_dir)
    for _, pattern in task_patterns:
        task_file = next((str(submission_path / f)
                         for f in os.listdir(submission_dir) if re.match(pattern, f)), None)
        filenames.append(task_file)
    return filenames

def is_valid_submission(submission_dir):
    """
    Check if the submission directory contains valid files.
    Returns True if there are at least 5 .py files and all task files are found.
    """
    py_files = [f for f in os.listdir(submission_dir) if f.endswith('.py')]
    if len(py_files) < 5:
        return False
        
    task_files = find_task_files(submission_dir)
    return all(task_files)  # Check if all tasks are found (no None values)

def relocate_files(submission_dir, is_valid):
    """
    Relocate files to either Renamed or Problem directory based on validation.
    """
    base_target = "Renamed" if is_valid else "Problem"
    submission_path = Path(submission_dir)
    target_dir = Path(f"./{base_target}") / submission_path.name
    
    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Move all files from submission directory to target directory
    for file in os.listdir(submission_dir):
        src_path = submission_path / file
        dst_path = target_dir / file
        shutil.move(str(src_path), str(dst_path))
    
    print(f"Moved {submission_dir} to {target_dir}")

def process_submissions(base_dir = "./Submissions"):
    """
    Process all submissions in the base_dir directory.
    """
    # Create Renamed and Problem directories if they don't exist
    try:
        ensure_dir("./Renamed")
        ensure_dir("./Problem")
        
        base_path = Path(base_dir)
        for submission_dir in base_path.glob('*'):
            if submission_dir.is_dir():
                is_valid = is_valid_submission(str(submission_dir))
                relocate_files(str(submission_dir), is_valid)
    except Exception as e:
        print(f"Error processing submissions: {e}")

if __name__ == "__main__":
    process_submissions()