import os, re

def rename_directories(directory='./Submissions01'):
    """
    Rename directories by extracting full name and submission date from directory names.
    Example:
    'assignment1 - submission - John Doe - Oct 15' -> 'John Doe - Oct 15'
    
    Args:
        directory (str): Path to the directory containing submission folders
    """
    for dir_name in os.listdir(directory):
        parts = dir_name.split(' - ')
        if len(parts) >= 4:
            full_name = parts[2].strip()
            submission_date = parts[3].strip()
            new_name = f"{full_name} - {submission_date}"
            os.rename(
                os.path.join(directory, dir_name),
                os.path.join(directory, new_name)
            )
            print(f"Renamed: {dir_name} -> {new_name}")


def check_duplicate_names(directory='./Submissions01'):
    """
    Check for duplicate student names in the submission directory.
    Example:
    If there are multiple submissions from 'John Doe', it will be reported.
    
    Args:
        directory (str): Path to the directory containing submission folders
    """
    names = {}
    pattern = re.compile(r'^(.*?)\s*-\s*(Oct|Nov)')

    for dir_name in os.listdir(directory):
        match = pattern.match(dir_name)
        if match:
            full_name = match.group(1).strip()
            names[full_name] = names.get(full_name, 0) + 1

    duplicates = [name for name, count in names.items() if count > 1]
    if duplicates:
        print("Duplicate names found:")
        for name in duplicates:
            print(name)


def rename_to_name_only(directory='./Submissions01'):
    """
    Rename directories to contain only the student's name.
    Example:
    'John Doe - Oct 15' -> 'John Doe'
    
    Args:
        directory (str): Path to the directory containing submission folders
    """
    pattern = re.compile(r'^(.*?)\s*-\s*(Oct|Nov)')

    for dir_name in os.listdir(directory):
        match = pattern.match(dir_name)
        if match:
            full_name = match.group(1).strip()
            new_name = full_name
            os.rename(
                os.path.join(directory, dir_name),
                os.path.join(directory, new_name)
            )
            print(f"Renamed: {dir_name} -> {new_name}")

if __name__ == "__main__":
    rename_directories()
    # check_duplicate_names()
    rename_to_name_only()