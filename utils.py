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

def extract(pattern: str, response: str, flags=re.DOTALL) -> str:
    """
    Extract content matching a regex pattern from a response string.
    
    Args:
        pattern: Regular expression pattern to match
        response: String to search in
        flags: Regular expression flags (default: re.DOTALL)
        
    Returns:
        Matched content as string, stripped of whitespace
    """
    match = re.search(pattern, response, flags)
    return match.group(1).strip() if match else ''


def parse_response(response: str, patterns: dict) -> dict:
    """
    Parse a response string according to provided patterns dictionary.
    
    Args:
        response: Response string to parse
        patterns: Dictionary of patterns to extract, can be nested
        
    Returns:
        Dictionary containing extracted values, with scores converted to float
    """
    result = {}
    for key, pattern in patterns.items():
        if isinstance(pattern, dict):
            # Handle nested patterns (e.g. reasoning/grade pairs)
            result[key] = {
                sub_key: extract(sub_pattern, response) 
                if 'reasoning' in sub_key 
                else float(extract(sub_pattern, response).replace('[', '').replace(']', '') or 0) 
                for sub_key, sub_pattern in pattern.items()
            }
        else:
            # Handle top-level patterns
            result[key] = (
                extract(pattern, response) 
                if 'score' not in key 
                else float(extract(pattern, response).replace('[', '').replace(']', '') or 0)
            )
    return result

def parse_question_one(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'loop_implementation': {
            'reasoning': r'<loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'multiple_calculation': {
            'reasoning': r'<multiple_calculation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<multiple_calculation>.*?<grade>([\d.]+)</grade>'
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
        'loop_implementation': {
            'reasoning': r'<loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'output_formatting': {
            'reasoning': r'<output_formatting>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output_formatting>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_three(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'text_handling': {
            'reasoning': r'<text_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<text_handling>.*?<grade>([\d.]+)</grade>'
        },
        'loop_implementation': {
            'reasoning': r'<loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'vowel_checking': {
            'reasoning': r'<vowel_checking>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<vowel_checking>.*?<grade>([\d.]+)</grade>'
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
        'loop_implementation': {
            'reasoning': r'<loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'score_categorization': {
            'reasoning': r'<score_categorization>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<score_categorization>.*?<grade>([\d.]+)</grade>'
        },
        'output': {
            'reasoning': r'<output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output>.*?<grade>([\d.]+)</grade>'
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
        'pattern_generation': {
            'reasoning': r'<pattern_generation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<pattern_generation>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)


def parse_question_six(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'input_handling': {
            'reasoning': r'<input_handling>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<input_handling>.*?<grade>([\d.]+)</grade>'
        },
        'nested_loop_implementation': {
            'reasoning': r'<nested_loop_implementation>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<nested_loop_implementation>.*?<grade>([\d.]+)</grade>'
        },
        'calculations': {
            'reasoning': r'<calculations>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<calculations>.*?<grade>([\d.]+)</grade>'
        },
        'output_formatting': {
            'reasoning': r'<output_formatting>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output_formatting>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)
