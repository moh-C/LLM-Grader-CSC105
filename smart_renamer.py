import os
import shutil
import re
import openai
from dotenv import load_dotenv
import glob

def find_task_files(submission_dir):
    # Load environment variables from .env file
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    # List all files in the directory
    all_files = os.listdir(submission_dir)
    
    # If there is only one file, print its name and return
    if len(all_files) == 1:
        print(f"Only one file found: {all_files[0]}")
        return
    
    # Send the file list to OpenAI GPT-4
    openai.api_key = openai_api_key
    response = openai.Client().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Given the following list of files: {all_files}, map them to task01.py, task02.py, ..., task05.py. Make sure this is a smart way of doing it. Use reasoning in <reason> and then give me the list in <mapping>. The mapping must be a list is the [old_name, new_name]. CRITICAL: If the file is not present, there obviously is no match for it. so there must be as many mappings as there are files."
            }
        ],
        max_tokens=750
    )
    
    pattern = r'\[\'(.*?)\', \'(.*?)\'\]'
    matches = re.findall(pattern, response.choices[0].message.content)
    
    # Create new directory if it doesn't exist
    renamed_dir = os.path.join(os.path.dirname(submission_dir), 'Renamed')
    os.makedirs(renamed_dir, exist_ok=True)
    
    # Rename files in the same directory with new names
    for old_name, new_name in matches:
        old_path = os.path.join(submission_dir, old_name)
        new_path = os.path.join(submission_dir, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

def relocate_files(submission_dir, target_dir):
    find_task_files(submission_dir)
    # Check if the target directory exists, if not, create it
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Get the list of all files in the submission directory
    files = os.listdir(submission_dir)
    
    # Move each file to the target directory
    for file in files:
        src_path = os.path.join(submission_dir, file)
        dst_path = os.path.join(target_dir, file)
        shutil.move(src_path, dst_path)
    
    print(f"All files have been relocated from {submission_dir} to {target_dir}")

# Process all directories in ./Submissions01
base_dir = ".\\Submissions01"
target_base_dir = ".\\rename"

for submission_dir in glob.glob(os.path.join(base_dir, '*')):
    if os.path.isdir(submission_dir):
        # Extract the subdirectory name
        sub_dir_name = os.path.basename(submission_dir)
        target_dir = os.path.join(target_base_dir, sub_dir_name)
        relocate_files(submission_dir, target_dir)