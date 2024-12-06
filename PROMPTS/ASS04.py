TASK01 = """Grade the following Python temperature filter program. Temperature Filter
Create a list of above-freezing temperatures from the given readings.

Instructions:
1. Create an empty list for above-freezing temperatures
2. Loop through the provided temperature list 
3. Add temperatures above 0°C to the new list
4. Print both original and filtered lists

Grading Rubric (Be Generous!)
- List initialization and loop: 40%
- Temperature filtering: 40% 
- Output formatting: 20%
- CRITICAL: We do NOT care about variable names or print formatting style
- CRITICAL: We do NOT care about code efficiency, just correct logic

Example Input/Output:
Input: temperatures = [-2, 5, -6, 3, -1, 8, 12, -4, 0, 7]
Output:
Original Temperatures: [-2, 5, -6, 3, -1, 8, 12, -4, 0, 7]
Above Freezing: [5, 3, 8, 12, 7]

<thinkpad>
Grade generously with these guidelines:
- List initialization and loop (40%): Award full marks if empty list is created and any working loop iterates through temperatures
- Temperature filtering (40%): Award full marks if code correctly identifies temperatures > 0°C
- Output formatting (20%): Award full marks if both lists are displayed in any readable format
When in doubt, award full marks - focus on working logic over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <list_and_loop>
            <reasoning>[Brief: Is empty list created and loop implemented?]</reasoning>
            <grade>[40 or 0]</grade>
        </list_and_loop>
        <temperature_filtering>
            <reasoning>[Brief: Does code correctly filter above 0°C?]</reasoning>
            <grade>[40 or 0]</grade>
        </temperature_filtering>
        <output>
            <reasoning>[Brief: Are both lists displayed?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working elements, suggest improvements for missing/incorrect parts. If meets all criteria, don't suggest improvement!]</final_feedback>
</evaluation>

Solution to Grade:
{solution}
"""

TASK02 = """Grade the following Python name sorting program. Name Sorter
Sort names into separate lists based on "Mr." or "Ms." prefix.

Instructions:
1. Create two empty lists for different prefixes (Mr. and Ms.)
2. Loop through the provided names list
3. Check each name's prefix and sort into appropriate list
4. Print both resulting lists

Grading Rubric (Be Generous!)
- List initialization and loop: 40%
- Prefix checking and sorting: 40%
- Output formatting: 20%
- CRITICAL: We do NOT care about variable names or print formatting style
- CRITICAL: We do NOT care about code efficiency, just correct logic

Example Input/Output:
Input: names = ['Ms.Emma', 'Mr.Noah', 'Ms.Olivia', 'Mr.Liam', 'Ms.Ava']
Output:
Female Students: ['Ms.Emma', 'Ms.Olivia', 'Ms.Ava']
Male Students: ['Mr.Noah', 'Mr.Liam']

<thinkpad>
Grade generously with these guidelines:
- List initialization and loop (40%): Award full marks if two empty lists are created and loop iterates through names
- Prefix checking and sorting (40%): Award full marks if code correctly identifies and sorts by 'Mr.' or 'Ms.' prefix
- Output formatting (20%): Award full marks if both sorted lists are displayed in any readable format
When in doubt, award full marks - focus on working logic over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <lists_and_loop>
            <reasoning>[Brief: Are two empty lists created and loop implemented?]</reasoning>
            <grade>[40 or 0]</grade>
        </lists_and_loop>
        <prefix_sorting>
            <reasoning>[Brief: Does code correctly sort by prefix?]</reasoning>
            <grade>[40 or 0]</grade>
        </prefix_sorting>
        <output>
            <reasoning>[Brief: Are both sorted lists displayed?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working elements, suggest improvements for missing/incorrect parts. If meets all criteria, don't suggest improvement!]</final_feedback>
</evaluation>

Solution to Grade:
{solution}
"""

TASK03 = """Grade the following Python grade calculator program. Grade Calculator
Calculate class average and find highest/lowest grades from a list of grades.

Instructions:
1. Calculate the sum of all grades
2. Find the average grade
3. Determine highest and lowest grades
4. Print all calculated results

Grading Rubric (Be Generous!)
- Calculation implementation: 40%
- Min/max finding: 40%
- Output formatting: 20%
- CRITICAL: We do NOT care about variable names or print formatting style
- CRITICAL: We do NOT care about code efficiency, just correct logic

Example Input/Output:
Input: grades = [85, 92, 78, 65, 88, 72, 90]
Output:
Class Average: 81.4
Highest Grade: 92
Lowest Grade: 65

<thinkpad>
Grade generously with these guidelines:
- Calculation implementation (40%): Award full marks if code correctly calculates sum and average
- Min/max finding (40%): Award full marks if code identifies highest and lowest grades in any way
- Output formatting (20%): Award full marks if all results are displayed in any readable format
When in doubt, award full marks - focus on working logic over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <calculations>
            <reasoning>[Brief: Are sum and average calculated correctly?]</reasoning>
            <grade>[40 or 0]</grade>
        </calculations>
        <minmax_finding>
            <reasoning>[Brief: Are highest and lowest grades found?]</reasoning>
            <grade>[40 or 0]</grade>
        </minmax_finding>
        <output>
            <reasoning>[Brief: Are all results displayed clearly?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working elements, suggest improvements for missing/incorrect parts. If meets all criteria, don't suggest improvement!]</final_feedback>
</evaluation>

Solution to Grade:
{solution}
"""


TASK04 = """Grade the following Python shopping list editor program. Shopping List Editor
Manage shopping lists by removing purchased items and adding new items.

Instructions:
1. Start with current shopping list
2. Remove purchased items
3. Add new items needed
4. Show final updated list

Grading Rubric (Be Generous!)
- Removing items: 30%
- Adding items: 30%
- List printing: 20%
- Output format: 20%
- CRITICAL: We do NOT care about variable names or print styling
- CRITICAL: We do NOT care about code efficiency, just correct logic

Example Input/Output:
Input:
Initial Shopping List: ['apple', 'milk', 'bread']
Items Purchased: ['milk']
New Items to Add: ['banana']

Output:
Final Shopping List: ['apple', 'bread', 'banana']

<thinkpad>
Grade generously with these guidelines:
- Removing items (30%): Award full marks if purchased items are correctly removed from list
- Adding items (30%): Award full marks if new items are successfully added to list
- List printing (20%): Award full marks if list is displayed in any readable format
- Output format (20%): Award full marks if final list matches expected structure
When in doubt, award full marks - focus on working logic over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <item_removal>
            <reasoning>[Brief: Are purchased items correctly removed?]</reasoning>
            <grade>[30 or 0]</grade>
        </item_removal>
        <item_addition>
            <reasoning>[Brief: Are new items successfully added?]</reasoning>
            <grade>[30 or 0]</grade>
        </item_addition>
        <list_printing>
            <reasoning>[Brief: Is list displayed clearly?]</reasoning>
            <grade>[20 or 0]</grade>
        </list_printing>
        <output_format>
            <reasoning>[Brief: Does output match expected format?]</reasoning>
            <grade>[20 or 0]</grade>
        </output_format>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working elements, suggest improvements for missing/incorrect parts. If meets all criteria, don't suggest improvement!]</final_feedback>
</evaluation>

Solution to Grade:
{solution}
"""


TASK05 = """Grade the following Python text message analyzer program. Text Message Analyzer
Analyze text messages for greeting patterns and urgency markers.

Instructions:
1. Count messages starting with "Hello" or "Hi"
2. Find the longest and shortest messages
3. Create list of messages containing "urgent"
4. Print all analysis results

Grading Rubric (Be Generous!)
- Message analysis: 40%
- Pattern matching: 40%
- Output formatting: 20%
- CRITICAL: We do NOT care about variable names or print styling
- CRITICAL: We do NOT care about code efficiency, just correct logic

Example Input/Output:
Input: messages = ["Hello! Meeting at 3pm", "urgent: Please call"]
Output:
Greeting Messages: 1
Urgent Messages: 1
Longest Message: "Hello! Meeting at 3pm" (20 chars)
Shortest Message: "urgent: Please call" (17 chars)

<thinkpad>
Grade generously with these guidelines:
- Message analysis (40%): Award full marks if code correctly counts greetings and finds message lengths
- Pattern matching (40%): Award full marks if code identifies urgent messages and greeting patterns
- Output formatting (20%): Award full marks if all analysis results are displayed clearly
When in doubt, award full marks - focus on working logic over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <message_analysis>
            <reasoning>[Brief: Are greetings counted and message lengths found?]</reasoning>
            <grade>[40 or 0]</grade>
        </message_analysis>
        <pattern_matching>
            <reasoning>[Brief: Are urgent messages and greetings identified?]</reasoning>
            <grade>[40 or 0]</grade>
        </pattern_matching>
        <output>
            <reasoning>[Brief: Are all results displayed clearly?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working elements, suggest improvements for missing/incorrect parts. If meets all criteria, don't suggest improvement!]</final_feedback>
</evaluation>

Solution to Grade:
{solution}
"""

TASK06 = """Grade the following Python text message analyzer program. Text Message Analyzer
Analyze text messages for greeting patterns and urgency markers.

Instructions:
1. Count messages starting with "Hello" or "Hi"
2. Find the longest and shortest messages
3. Create list of messages containing "urgent"
4. Print all analysis results

Grading Rubric (Be Generous!)
- Message analysis: 40%
- Pattern matching: 40%
- Output formatting: 20%
- CRITICAL: We do NOT care about variable names or print styling
- CRITICAL: We do NOT care about code efficiency, just correct logic

Example Input/Output:
Input: messages = ["Hello! Meeting at 3pm", "urgent: Please call"]
Output:
Greeting Messages: 1
Urgent Messages: 1
Longest Message: "Hello! Meeting at 3pm" (20 chars)
Shortest Message: "urgent: Please call" (17 chars)

<thinkpad>
Grade generously with these guidelines:
- Message analysis (40%): Award full marks if code correctly counts greetings and finds message lengths
- Pattern matching (40%): Award full marks if code identifies urgent messages and greeting patterns
- Output formatting (20%): Award full marks if all analysis results are displayed clearly
When in doubt, award full marks - focus on working logic over exact syntax
</thinkpad>

<evaluation>
    <criteria_assessment>
        <message_analysis>
            <reasoning>[Brief: Are greetings counted and message lengths found?]</reasoning>
            <grade>[40 or 0]</grade>
        </message_analysis>
        <pattern_matching>
            <reasoning>[Brief: Are urgent messages and greetings identified?]</reasoning>
            <grade>[40 or 0]</grade>
        </pattern_matching>
        <output>
            <reasoning>[Brief: Are all results displayed clearly?]</reasoning>
            <grade>[20 or 0]</grade>
        </output>
    </criteria_assessment>
    <final_score>[Total]</final_score>
    <final_feedback>[Max 25 words: Note working elements, suggest improvements for missing/incorrect parts. If meets all criteria, don't suggest improvement!]</final_feedback>
</evaluation>

Solution to Grade:
{solution}
"""