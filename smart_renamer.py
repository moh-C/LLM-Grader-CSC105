import os
import asyncio
from llm import LLM

RENAME_PROMPT = """Given these filenames:
{files}

Please map them to Task01.py through Task06.py based on the filename patterns. 
In <reason>, explain your mapping logic.
Then in <mapping>, provide the mappings in this exact format (one per line):
old_filename.py -> new_filename.py

Instructions: Be concise and super critical. Look for numbers and task indicators in filenames.
If unsure about any mapping, say "UNSURE" and do not output any mappings.
"""

def sanitize_filename(filename):
    # Remove any quotes or problematic characters
    return filename.strip().strip('"\'')

def extract_rename_pairs(response):
    """Extract filename mapping pairs from LLM response."""
    pairs = []
    for line in response.split('\n'):
        if '->' in line:
            old_name, new_name = line.split('->')
            # Clean up any whitespace and ensure .py extension
            old_name = old_name.strip()
            new_name = new_name.strip()
            if not old_name.endswith('.py'):
                old_name += '.py'
            if not new_name.endswith('.py'):
                new_name += '.py'
            pairs.append((old_name, new_name))
    return pairs

async def process_directory(directory):
    # Initialize LLM
    llm = LLM(
        prompt_template=RENAME_PROMPT,
        system_message="You are a file renaming assistant. Analyze filename patterns to determine correct task numbers.",
        model="gpt-4o-mini"
    )
    
    print(f"\nProcessing directory: {directory}")
    
    # Get all Python files in directory
    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    if not files:
        print(f"No Python files found in {directory}")
        return

    # Get LLM response with just filenames
    try:
        response = await llm.get_response_with_prompt(RENAME_PROMPT.format(files="\n".join(files)))
    except Exception as e:
        print(f"Error getting LLM response: {str(e)}")
        return
    
    if "UNSURE" in response:
        print(f"LLM is unsure about mappings in {directory}, skipping...")
        return
        
    print("\nProposed changes:")
    print(response)
    
    # Ask for user confirmation
    confirmation = input("\nProceed with these renames? (y/n): ").lower()
    if confirmation != 'y':
        print("Skipping directory...")
        return

    # Extract and execute rename commands
    rename_pairs = extract_rename_pairs(response)
    for old_name, new_name in rename_pairs:
        old_name = sanitize_filename(old_name)
        new_name = sanitize_filename(new_name)
        
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        
        if not os.path.exists(old_path):
            print(f"Source file not found: {old_path}")
            continue
            
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {old_name}: {str(e)}")

async def main():
    base_dir = "./Problem"
    directories = [os.path.join(base_dir, d) for d in os.listdir(base_dir) 
                  if os.path.isdir(os.path.join(base_dir, d))]
    
    for directory in directories:
        await process_directory(directory)

if __name__ == "__main__":
    asyncio.run(main())