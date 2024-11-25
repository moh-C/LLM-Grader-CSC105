import re

def strip_comments(filename: str) -> str:
    """Reads a Python file and returns code without comments."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Strip inline and full-line comments while preserving strings
    code_lines = []
    in_multiline = False
    multiline_quote = None
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Handle multiline strings
        if multiline_quote and line.strip().endswith(multiline_quote):
            in_multiline = False
            multiline_quote = None
            code_lines.append(line)
            continue
            
        if in_multiline:
            code_lines.append(line)
            continue
            
        # Check for multiline string start
        if '"""' in line or "'''" in line:
            if '"""' in line:
                if line.count('"""') == 1:
                    in_multiline = True
                    multiline_quote = '"""'
            if "'''" in line:
                if line.count("'''") == 1:
                    in_multiline = True
                    multiline_quote = "'''"
            code_lines.append(line)
            continue
        
        # Remove full-line comments
        if line.lstrip().startswith('#'):
            continue
            
        # Handle inline comments while preserving strings
        modified_line = ''
        in_string = False
        string_char = None
        i = 0
        
        while i < len(line):
            char = line[i]
            
            # Handle string literals
            if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                modified_line += char
                
            # Handle comments
            elif char == '#' and not in_string:
                break
                
            else:
                modified_line += char
                
            i += 1
        
        # Add non-empty lines
        if modified_line.strip():
            code_lines.append(modified_line)
    
    return ''.join(code_lines)

import json, csv, os, shutil

def save_responses_json(responses, student_name):
    """
    Save the responses from LLM agents to a JSON file.
    """
    filename = f"Graded/{'_'.join(student_name)}.json"
    with open(filename, 'w') as f:
        json.dump(responses, f, indent=4)

    # Also save as .txt file
    txt_filename = f"Graded/{'_'.join(student_name)}.txt"
    with open(txt_filename, 'w') as f:
        for response in responses:
            f.write(json.dumps(response, indent=4))
            f.write('\n')


def calculate_final_grade(responses):
    """
    Calculate the final grade based on individual task scores and their weights.
    """
    weights = [0.20, 0.20, 0.20, 0.20, 0.20, 0.20]
    scores = [int(response['final_score']) for response in responses]
    weighted_final = sum(score * weight for score, weight in zip(scores, weights))
    # Cap the weighted final score at 100
    weighted_final = min(100, weighted_final)
    return scores + [round(weighted_final)]

def save_scores_csv(scores, student_name):
    """
    Save the scores to a CSV file.
    """
    csv_file = 'Scores.csv'
    headers = ['First Name', 'Last Name', 'Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6', 'Final Grade']
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


def calculate_final_grade(responses):
    """
    Calculate the final grade based on individual task scores and their weights.
    """
    weights = [0.20, 0.20, 0.20, 0.20, 0.20, 0.20]
    scores = [int(response['final_score']) for response in responses]
    weighted_final = sum(score * weight for score, weight in zip(scores, weights))
    # Cap the weighted final score at 100
    weighted_final = min(100, weighted_final)
    return scores + [round(weighted_final)]


def find_task_files(submission_dir):
    """
    Find task files in the submission directory based on predefined patterns.
    """
    task_patterns = [
        (1, r'(?i)(task\s*0?1|assignment\d*task\s*0?1|Task\s*1)\.py$'),
        (2, r'(?i)(task\s*0?2|assignment\d*task\s*0?2|Task\s*2)\.py$'),
        (3, r'(?i)(task\s*0?3|assignment\d*task\s*0?3|Task\s*3)\.py$'),
        (4, r'(?i)(task\s*0?4|assignment\d*task\s*0?4|Task\s*4)\.py$'),
        (5, r'(?i)(task\s*0?5|assignment\d*task\s*0?5|Task\s*5)\.py$'),
        (6, r'(?i)(task\s*0?6|assignment\d*task\s*0?6|Task\s*6)\.py$')
    ]
    filenames = []
    for _, pattern in task_patterns:
        task_file = next((os.path.join(submission_dir, f).replace('/', '\\')
                         for f in os.listdir(submission_dir) if re.match(pattern, f)), None)
        filenames.append(task_file)
    return filenames


def extract_student_name(submission_dir):
    """
    Extract the student's name from the submission directory name.
    """
    base_name = os.path.basename(submission_dir)
    parts = base_name.strip().split()
    return [parts[0], parts[1]] if len(parts) >= 2 else [base_name, ""]