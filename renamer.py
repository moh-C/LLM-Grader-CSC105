import os, re

def remove_assignment_prefix(directory='./Submissions'):
    """Transform 'assignment1 - submission - John Doe - Oct 15' to 'John Doe - Oct 15'"""
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

def find_multiple_submissions(directory='./Submissions'):
    """Find students who submitted multiple times"""
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

def remove_submission_dates(directory='./Submissions'):
    """Transform 'John Doe - Oct 15' to 'John Doe'"""
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

def process_submission_directories(directory='./Submissions'):
    """
    Process submission directories in the following order:
    1. Clean up directory names by removing assignment prefixes
    2. Check for multiple submissions from same student
    3. Optionally remove submission dates (commented by default)
    """
    print("Step 1: Removing assignment prefixes...")
    remove_assignment_prefix(directory)
    
    print("\nStep 2: Checking for multiple submissions...")
    find_multiple_submissions(directory)
    
    # print("\nStep 3: Removing submission dates...")
    # remove_submission_dates(directory)

if __name__ == "__main__":
    process_submission_directories()