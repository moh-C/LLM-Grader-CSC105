# LLM-Grader-CSC105

# Folder Structure
- `llm.py`: Main LLM class
- `./Submissions`: Is the submission directory
- `./Duplicates`: Find all the problematic files here
- `./Done`: If a file is done, dump it in here
- `./PROMPTS`: Contains the prompts and the prompt processor for a particular assignment
- `./Graded`: Contains the JSON files which are result of grading
- `./Renamed`: After renaming, all the files will be here (renamed to contain TASK01 to TASK06)

# Renamer
First of all, we want to start withe the renamer. Rename the directories so that we know about the duplicates and stuff like that.

## Step 1
For this, we use `renamer.py`. 

This file has 3 steps:
Process submission directories in the following order:
1. Clean up directory names by removing assignment prefixes
2. Check for multiple submissions from same student
3. Optionally remove submission dates (commented by default)

## Step 2
`content_checker.py`. We need the files to have TASK01-TASK06 formats.
If there is a problem, dump them into `./Problem`
If not, dump them into `./Renamed`