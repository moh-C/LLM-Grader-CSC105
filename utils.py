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

def extract(pattern, response, flags=re.DOTALL):
    match = re.search(pattern, response, flags)
    return match.group(1).strip() if match else ''

def parse_response(response: str, patterns: dict) -> dict:
    result = {}
    for key, pattern in patterns.items():
        if isinstance(pattern, dict):
            result[key] = {sub_key: extract(sub_pattern, response) if 'reasoning' in sub_key else float(extract(sub_pattern, response).replace('[', '').replace(']', '') or 0) for sub_key, sub_pattern in pattern.items()}
        else:
            result[key] = extract(pattern, response) if 'score' not in key else float(extract(pattern, response).replace('[', '').replace(']', '') or 0)
    return result

def parse_question_one(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'input_handling': {
            'reasoning': r'<input_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<input_handling>.*?<grade>([\d.]+)</grade>'
        },
        'calculation': {
            'reasoning': r'<calculation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<calculation>.*?<grade>([\d.]+)</grade>'
        },
        'variable_naming': {
            'reasoning': r'<variable_naming>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<variable_naming>.*?<grade>([\d.]+)</grade>'
        },
        'output': {
            'reasoning': r'<output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_two(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'input_handling': {
            'reasoning': r'<input_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<input_handling>.*?<grade>([\d.]+)</grade>'
        },
        'if_statement': {
            'reasoning': r'<if_statement>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<if_statement>.*?<grade>([\d.]+)</grade>'
        },
        'pass_output': {
            'reasoning': r'<pass_output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<pass_output>.*?<grade>([\d.]+)</grade>'
        },
        'fail_output': {
            'reasoning': r'<fail_output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<fail_output>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_three(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'input_handling': {
            'reasoning': r'<input_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<input_handling>.*?<grade>([\d.]+)</grade>'
        },
        'loop_implementation': {
            'reasoning': r'<loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'sum_calculation': {
            'reasoning': r'<sum_calculation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<sum_calculation>.*?<grade>([\d.]+)</grade>'
        },
        'average_calculation': {
            'reasoning': r'<average_calculation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<average_calculation>.*?<grade>([\d.]+)</grade>'
        },
        'max_number': {
            'reasoning': r'<max_number>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<max_number>.*?<grade>([\d.]+)</grade>'
        },
        'min_number': {
            'reasoning': r'<min_number>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<min_number>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_four(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'input_handling': {
            'reasoning': r'<input_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<input_handling>.*?<grade>([\d.]+)</grade>'
        },
        'conditional_structure': {
            'reasoning': r'<conditional_structure>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<conditional_structure>.*?<grade>([\d.]+)</grade>'
        },
        'basic_operations': {
            'reasoning': r'<basic_operations>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<basic_operations>.*?<grade>([\d.]+)</grade>'
        },
        'division_handling': {
            'reasoning': r'<division_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<division_handling>.*?<grade>([\d.]+)</grade>'
        },
        'output_format': {
            'reasoning': r'<output_format>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output_format>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_five(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'input_handling': {
            'reasoning': r'<input_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<input_handling>.*?<grade>([\d.]+)</grade>'
        },
        'loop_implementation': {
            'reasoning': r'<loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'even_odd_check': {
            'reasoning': r'<even_odd_check>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<even_odd_check>.*?<grade>([\d.]+)</grade>'
        },
        'counting_logic': {
            'reasoning': r'<counting_logic>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<counting_logic>.*?<grade>([\d.]+)</grade>'
        },
        'output_display': {
            'reasoning': r'<output_display>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output_display>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)
