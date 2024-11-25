TASK01 = """Grade the following Python multiples counter program. Multiples Counter
Print all multiples of 3 less than 100.

Instructions:
- Write a loop to iterate through numbers
- Calculate multiples of 3 using the loop variable
- Check if the multiple is less than 100 and print if true

Grading Rubric (Be Generous!)
- Loop implementation: 40%
- Multiple calculation: 40%
- Output: 20%
- CRITICAL: We do NOT care about print formatting, just the logic! and a simple format is fine (when printing).
- CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

Output Format:
<thinkpad>
Grade generously with these guidelines:
- Loop implementation (40%): Award full marks if any working loop is used
- Multiple calculation (40%): Award full marks if code identifies multiples of 3 in any way
- Output (20%): Award full marks if correct multiples are displayed in any format
When in doubt, award full marks - focus on working code over exact syntax

</thinkpad>
<evaluation>
    <criteria_assessment>
        <loop_implementation>
            <reasoning>[Brief: Is a working loop implemented?]</reasoning>
            <grade>[40 or 0]</grade>
        </loop_implementation>
        <multiple_calculation>
            <reasoning>[Brief: Does code identify multiples of 3?]</reasoning>
            <grade>[40 or 0]</grade>
        </multiple_calculation>
        <output>
            <reasoning>[Brief: Are correct multiples displayed?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>
Solution to Grade
{solution}
"""

TASK02 = """Grade the following Python pattern printer program.
Create a rectangle pattern with user-specified dimensions and symbol.

Instructions:
- Get an integer number from user for rows
- Get an integer number from user for columns
- Get a symbol from user
- Create nested loops to print the pattern

Grading Rubric (Be Generous!)
- Input handling: 30%
- Loop implementation: 40%
- Output formatting: 30%
- CRITICAL: We do NOT care about input validation, just the logic! Any form of input collection is fine.
- CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

Output Format
<thinkpad>
Grade generously with these guidelines:
- Input handling (30%): Award full marks if all three inputs (rows, columns, symbol) are collected
- Loop implementation (40%): Award full marks if nested loops create the pattern in any way
- Output formatting (30%): Award full marks if pattern displays in rectangular shape
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>
<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Brief: Are all three inputs collected?]</reasoning>
            <grade>[30 or 0]</grade>
        </input_handling>
        <loop_implementation>
            <reasoning>[Brief: Are nested loops used to create pattern?]</reasoning>
            <grade>[40 or 0]</grade>
        </loop_implementation>
        <output_formatting>
            <reasoning>[Brief: Does output form a proper rectangle?]</reasoning>
            <grade>[30 or 0]</grade>
        </output_formatting>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>
Solution to Grade
{solution}
"""

TASK03 = """Grade the following Python vowel counter program. Vowel Counter
Count vowels in a given text string.

Instructions:
Use the provided text string
- Initialize a counter variable as 'count'
- Create a loop to process each character
- Check if each character is a vowel
- Print the final count

Grading Rubric (Be Generous!)
- Text handling: 20%
- Loop implementation: 40%
- Vowel checking: 40%
- CRITICAL: We do NOT care about case sensitivity or special vowels (é,ë,etc), just basic vowels (a,e,i,o,u)!
- CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

Output Format
<thinkpad>
Grade generously with these guidelines:
- Text handling (20%): Award full marks if program uses provided text string
- Loop implementation (40%): Award full marks if any loop processes the characters
- Vowel checking (40%): Award full marks if code identifies basic vowels in any way
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>
<evaluation>
    <criteria_assessment>
        <text_handling>
            <reasoning>[Brief: Is provided text string used?]</reasoning>
            <grade>[20 or 0]</grade>
        </text_handling>
        <loop_implementation>
            <reasoning>[Brief: Is a loop used to process characters?]</reasoning>
            <grade>[40 or 0]</grade>
        </loop_implementation>
        <vowel_checking>
            <reasoning>[Brief: Does code check for vowels?]</reasoning>
            <grade>[40 or 0]</grade>
        </vowel_checking>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>
Solution to Grade
{solution}
"""

TASK04 =  """Grade the following Python score analyzer program. Score Analyzer

Analyze a set of test scores and categorize them.

Instructions:
- Get number of scores to analyze from user as 'num_scores'
- Create three counter variables (below_passing, passing, excellent)
- Create a loop to get each score
- Categorize each score using if-elif-else
- Print final counts for each category

Grading Rubric (Be Generous!)
- Input handling: 25%
- Loop implementation: 35%
- Score categorization: 30%
- Output: 10%
- CRITICAL: We do NOT care about input validation or exact category thresholds, just the logic of categorization!
- CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

Output Format
<thinkpad>
Grade generously with these guidelines:
- Input handling (25%): Award full marks if program collects number of scores and scores
- Loop implementation (35%): Award full marks if loop collects scores in any way
- Score categorization (30%): Award full marks if scores are sorted into three categories
- Output (10%): Award full marks if category counts are displayed
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>
<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Brief: Are number of scores and scores collected?]</reasoning>
            <grade>[25 or 0]</grade>
        </input_handling>
        <loop_implementation>
            <reasoning>[Brief: Is a loop used to collect scores?]</reasoning>
            <grade>[35 or 0]</grade>
        </loop_implementation>
        <score_categorization>
            <reasoning>[Brief: Are scores categorized into three groups?]</reasoning>
            <grade>[30 or 0]</grade>
        </score_categorization>
        <output>
            <reasoning>[Brief: Are category counts displayed?]</reasoning>
            <grade>[10 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>
Solution to Grade
{solution}
"""

TASK05 = """Grade the following Python letter pattern program. Letter Pattern.
Create a pattern where each letter repeats based on its position.

Instructions:
- Get number of positions from user as 'N'
- Create alphabet string
- Create loop for positions
- Get correct letter for each position
- Print letter repeated position times

Grading Rubric (Be Generous!)

- Input handling: 30%
- Loop implementation: 40%
- Pattern generation: 30%
- CRITICAL: We do NOT care about case sensitivity or exact alphabet representation method!
- CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

Output Format
<thinkpad>
Grade generously with these guidelines:
- Input handling (30%): Award full marks if program gets number of positions
- Loop implementation (40%): Award full marks if loop creates pattern in any way
- Pattern generation (30%): Award full marks if letters repeat based on position
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>
<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Brief: Is number of positions collected?]</reasoning>
            <grade>[30 or 0]</grade>
        </input_handling>
        <loop_implementation>
            <reasoning>[Brief: Is a loop used to create pattern?]</reasoning>
            <grade>[40 or 0]</grade>
        </loop_implementation>
        <pattern_generation>
            <reasoning>[Brief: Do letters repeat correctly by position?]</reasoning>
            <grade>[30 or 0]</grade>
        </pattern_generation>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>
Solution to Grade
{solution}
"""

TASK06 = """Grade the following Python reaction time analysis program. Reaction Time Analysis
Analyze reaction times for multiple participants.

Instructions:
- Get participant count and trials per participant
- Create outer loop for participants
- Initialize variables for each participant
- Create inner loop for trials
- Process each trial time
- Calculate and print statistics per participant
- Format output properly

Grading Rubric (Be Generous!):
- Input handling: 20%
- Nested loop implementation: 35%
- Calculations: 35%
- Output formatting: 10%
- CRITICAL: We do NOT care about specific statistical methods, any reasonable calculation is fine!
- CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

Output Format
<thinkpad>
Grade generously with these guidelines:
- Input handling (20%): Award full marks if participant and trial counts are collected
- Nested loop implementation (35%): Award full marks if nested loops process participants and trials
- Calculations (35%): Award full marks if basic statistics are calculated per participant
- Output formatting (10%): Award full marks if results are displayed per participant
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>
<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Brief: Are participant and trial counts collected?]</reasoning>
            <grade>[20 or 0]</grade>
        </input_handling>
        <nested_loop_implementation>
            <reasoning>[Brief: Are nested loops used for participants and trials?]</reasoning>
            <grade>[35 or 0]</grade>
        </nested_loop_implementation>
        <calculations>
            <reasoning>[Brief: Are statistics calculated per participant?]</reasoning>
            <grade>[35 or 0]</grade>
        </calculations>
        <output_formatting>
            <reasoning>[Brief: Are results displayed per participant?]</reasoning>
            <grade>[10 or 0]</grade>
        </output_formatting>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>
Solution to Grade
{solution}
"""