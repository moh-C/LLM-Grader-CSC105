TASK01 = """Grade the following Python time conversion program.

# Task Details
Task 1: Time Conversion
Convert hours, minutes, and seconds to total seconds.
Instructions:
1. Get hours from the user and store it in a variable 
2. Get minutes from the user and store it in a variable
3. Get seconds from the user and store it in a variable 
4. Calculate the total seconds
5. Print the total seconds

# Grading Rubric (Be Generous!)
• Input handling: 20%
• Calculation accuracy: 40%
• Variable names (descriptive, not single letters): 20% 
• Output: 20%
• CRITICAL: We do NOT care about print formatting, just the logic! and a simple format is fine (when printing).
• CRITICAL: We do NOT care about code efficincy or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

# Output Format
<thinkpad>
Grade generously with these guidelines:
• Input handling (20%): Award full marks if inputs are collected, even if variable names differ
• Calculation (40%): Award full marks if total seconds formula is implemented in any way
• Variable naming (20%): Award full marks for descriptive names, penalize only single-letter variables
• Output (20%): Award full marks if result is displayed in any format
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Brief: Does code collect all three time inputs?]</reasoning>
            <grade>[20 or 0]</grade>
        </input_handling>
        <calculation>
            <reasoning>[Brief: Is seconds conversion formula implemented?]</reasoning>
            <grade>[40 or 0]</grade>
        </calculation>
        <variable_naming>
            <reasoning>[Brief: Are variables descriptively named?]</reasoning>
            <grade>[20 or 0]</grade>
        </variable_naming>
        <output>
            <reasoning>[Brief: Is result displayed?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all the criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>

# Solution to Grade
{solution}
"""

TASK02 = """Grade the following Python pass/fail determination program.

# Task Details
Task 2: Pass/Fail Grade Determination
Determine if a student passes or fails based on their grade.
Instructions:
1. Ask the user to enter their grade and store it in a variable
2. Use an 'if' statement to check if the grade is greater than or equal to 70
3. Print "Pass" if the condition is true, otherwise print "Fail"

# Grading Rubric (Be Generous!)
• Input handling: 25%
• If statement: 40%
• Pass output: 17.5%
• Fail output: 17.5%
• CRITICAL: We do NOT care about print formatting, just the logic! A simple format is fine (when printing).
• CRITICAL: We do NOT care about code efficiency or inefficiency, just the logic! So long as the logic is fine, full grade for that part!

# Output Format
<thinkpad>
Grade generously with these guidelines:
• Input handling (25%): Award full marks if any input is taken and stored, even if variable name differs
• If statement (40%): Award full marks if any if-else logic checks for passing condition (70 or similar threshold)
• Pass output (17.5%): Accept any variation of pass message ("Pass", "PASS", "Passed", etc.)
• Fail output (17.5%): Accept any variation of fail message ("Fail", "FAIL", "Failed", etc.)
When in doubt, award full marks - focus on working code over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Brief: Does code take input in any way?]</reasoning>
            <grade>[25 or 0]</grade>
        </input_handling>
        <if_statement>
            <reasoning>[Brief: Is there an if statement checking for passing condition?]</reasoning>
            <grade>[40 or 0]</grade>
        </if_statement>
        <pass_output>
            <reasoning>[Brief: Does it indicate passing in any way?]</reasoning>
            <grade>[17.5 or 0]</grade>
        </pass_output>
        <fail_output>
            <reasoning>[Brief: Does it indicate failing in any way?]</reasoning>
            <grade>[17.5 or 0]</grade>
        </fail_output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working operations, suggest improvements for missing/incorrect elements. If meets all the criteria, don't suggest improvement or reformatting!]</final_feedback>
</evaluation>

# Solution to Grade
{solution}
"""

TASK03 = """Grade the following Python sequence analysis program.

# Task Details
Task 3: Number Sequence Analysis
Get numbers from user, calculate sum, average, max, and min.
Instructions:
1. Get number count from user
2. Get that many numbers from user
3. Calculate: sum, average, max, min
4. Print the results

# Grading Rubric (Very Lenient!)
• Input handling: 20%
• Loop implementation: 20%
• Sum calculation: 15%
• Average calculation: 15%
• Max number: 15%
• Min number: 15%

CRITICAL GRADING NOTES:
• Code efficiency DOESN'T matter - if it works, it works!
• Variable names can be different (e.g., 'num_count' instead of 'count' is fine)
• Multiple loops or if statements are fine
• Print formatting doesn't matter
• Any working approach gets full marks for that section

# Solution to Grade
{solution}

# Output Format
<thinkpad>
Very lenient grading:
• Input (20%): Gets count and numbers somehow
• Loop (20%): Collects multiple numbers somehow
• Sum (15%): Any working sum method
• Average (15%): Any working average calculation
• Max (15%): Finds largest by any method
• Min (15%): Finds smallest by any method
If it works at all, give full marks for that section
</thinkpad>

<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Gets input numbers?]</reasoning>
            <grade>[20 or 0]</grade>
        </input_handling>
        <loop_implementation>
            <reasoning>[Collects multiple numbers?]</reasoning>
            <grade>[20 or 0]</grade>
        </loop_implementation>
        <sum_calculation>
            <reasoning>[Calculates sum somehow?]</reasoning>
            <grade>[15 or 0]</grade>
        </sum_calculation>
        <average_calculation>
            <reasoning>[Calculates average somehow?]</reasoning>
            <grade>[15 or 0]</grade>
        </average_calculation>
        <max_number>
            <reasoning>[Finds largest somehow?]</reasoning>
            <grade>[15 or 0]</grade>
        </max_number>
        <min_number>
            <reasoning>[Finds smallest somehow?]</reasoning>
            <grade>[15 or 0]</grade>
        </min_number>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Only suggest improvements if something is completely missing/wrong]</final_feedback>
</evaluation>"""

TASK04 = """Grade the following Python calculator program.

# Task Details
Task 4: Basic Calculator
Make a calculator that:
1. Gets two numbers from user
2. Gets an operator (+, -, *, /)
3. Calculates the result
4. Handles division by zero

# Grading Rubric (Very Lenient!)
• Input handling: 15%
• If-elif usage: 25%
• Basic operations (+,-,*): 25%
• Division and zero check: 25%
• Output: 10%

CRITICAL GRADING NOTES:
• Code efficiency DOESN'T matter - if it works, it works!
• Variable names can be different (e.g., 'first_num' instead of 'num1' is fine)
• Multiple if statements are fine
• Print formatting doesn't matter
• Any working approach gets full marks for that section

# Solution to Grade
{solution}

# Output Format
<thinkpad>
Very lenient grading:
• Input (15%): Gets 2 numbers and operator somehow
• If-elif (25%): Uses any conditional structure for operators
• Basic math (25%): Can do +, -, * operations
• Division (25%): Can divide and has any zero check
• Output (10%): Shows result somehow
If it works at all, give full marks for that section
</thinkpad>

<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Gets numbers and operator?]</reasoning>
            <grade>[15 or 0]</grade>
        </input_handling>
        <conditional_structure>
            <reasoning>[Has conditionals for operators?]</reasoning>
            <grade>[25 or 0]</grade>
        </conditional_structure>
        <basic_operations>
            <reasoning>[Does +,-,* work?]</reasoning>
            <grade>[25 or 0]</grade>
        </basic_operations>
        <division_handling>
            <reasoning>[Division works with zero check?]</reasoning>
            <grade>[25 or 0]</grade>
        </division_handling>
        <output_format>
            <reasoning>[Shows result?]</reasoning>
            <grade>[10 or 0]</grade>
        </output_format>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Only suggest improvements if something is completely missing/wrong]</final_feedback>
</evaluation>"""


TASK05 = """Grade the following Python even/odd counter program.

# Task Details
Task 5: Even/Odd Counter
Count how many even and odd numbers exist between two numbers.
1. Get start and end numbers
2. Count evens and odds between them
3. Show the counts

# Grading Rubric (Very Lenient!)
• Input handling: 20%
• Loop implementation: 30%
• Even/odd checking: 30%
• Counting: 15%
• Output: 5%

CRITICAL GRADING NOTES:
• Code efficiency DOESN'T matter - if it works, it works!
• Variable names can be different (e.g., 'beginning' instead of 'start' is fine)
• Multiple loops are fine
• Print formatting doesn't matter
• Any working approach gets full marks for that section

# Solution to Grade
{solution}

# Output Format
<thinkpad>
Very lenient grading:
• Input (20%): Gets start and end numbers somehow
• Loop (30%): Loops through numbers somehow
• Even/odd (30%): Can tell even from odd (using any method)
• Counting (15%): Keeps track of counts somehow
• Output (5%): Shows the counts somehow
If it works at all, give full marks for that section
</thinkpad>

<evaluation>
    <criteria_assessment>
        <input_handling>
            <reasoning>[Gets two numbers?]</reasoning>
            <grade>[20 or 0]</grade>
        </input_handling>
        <loop_implementation>
            <reasoning>[Loops through numbers?]</reasoning>
            <grade>[30 or 0]</grade>
        </loop_implementation>
        <even_odd_check>
            <reasoning>[Can identify even/odd?]</reasoning>
            <grade>[30 or 0]</grade>
        </even_odd_check>
        <counting_logic>
            <reasoning>[Keeps even/odd counts?]</reasoning>
            <grade>[15 or 0]</grade>
        </counting_logic>
        <output_display>
            <reasoning>[Shows both counts?]</reasoning>
            <grade>[5 or 0]</grade>
        </output_display>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Only suggest improvements if something is completely missing/wrong]</final_feedback>
</evaluation>"""