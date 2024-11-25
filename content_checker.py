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
    Find task files in the submission directory.
    Only accepts files named like: Task1.py, task01.py, Task01.py, task1.py
    """
    valid_pattern = r'^[Tt]ask0?[1-5]\.py$'
    task_files = [None] * 5  # Initialize list with None values
    
    for file in os.listdir(submission_dir):
        if re.match(valid_pattern, file):
            # Extract task number from filename
            task_num = int(re.search(r'[1-5]', file).group()) - 1
            task_files[task_num] = str(Path(submission_dir) / file)
            
    return task_files

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