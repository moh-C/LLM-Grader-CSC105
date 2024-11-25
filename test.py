import os
import re
import shutil

def check_task_files(root_dir):
    """
    Check all subdirectories for proper task file naming conventions.
    Moves directories with incorrectly named task files to ./Problem directory.
    """
    # Valid task file patterns
    valid_patterns = [
        r'^[Tt]ask0?[1-6]\.py$'  # Matches Task01.py, task1.py, etc.
    ]

    # Create Problem directory if it doesn't exist
    problem_dir = "./Problem"
    os.makedirs(problem_dir, exist_ok=True)

    # Go through each directory in the root
    for dir_path, _, files in os.walk(root_dir, topdown=False):
        if dir_path == root_dir or dir_path == problem_dir:
            continue

        py_files = [f for f in files if f.endswith('.py')]
        
        if py_files:  # Only check directories containing .py files
            has_invalid = False
            for file in py_files:
                # Check if file matches any valid pattern
                if not any(re.match(pattern, file) for pattern in valid_patterns):
                    has_invalid = True
                    break
            
            if has_invalid:
                # Move the directory to Problem folder
                dir_name = os.path.basename(dir_path)
                dest_path = os.path.join(problem_dir, dir_name)
                shutil.move(dir_path, dest_path)

# Example usage
if __name__ == "__main__":
    root_directory = "./Renamed/"  # Current directory, change this as needed
    check_task_files(root_directory)