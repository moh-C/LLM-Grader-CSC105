import re

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
        'list_and_loop': {
            'reasoning': r'<list_and_loop>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<list_and_loop>.*?<grade>([\d.]+)</grade>'
        },
        'temperature_filtering': {
            'reasoning': r'<temperature_filtering>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<temperature_filtering>.*?<grade>([\d.]+)</grade>'
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
        'lists_and_loop': {
            'reasoning': r'<lists_and_loop>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<lists_and_loop>.*?<grade>([\d.]+)</grade>'
        },
        'prefix_sorting': {
            'reasoning': r'<prefix_sorting>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<prefix_sorting>.*?<grade>([\d.]+)</grade>'
        },
        'output': {
            'reasoning': r'<output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_three(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'calculations': {
            'reasoning': r'<calculations>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<calculations>.*?<grade>([\d.]+)</grade>'
        },
        'minmax_finding': {
            'reasoning': r'<minmax_finding>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<minmax_finding>.*?<grade>([\d.]+)</grade>'
        },
        'output': {
            'reasoning': r'<output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)

def parse_question_four(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'item_removal': {
            'reasoning': r'<item_removal>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<item_removal>.*?<grade>([\d.]+)</grade>'
        },
        'item_addition': {
            'reasoning': r'<item_addition>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<item_addition>.*?<grade>([\d.]+)</grade>'
        },
        'list_printing': {
            'reasoning': r'<list_printing>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<list_printing>.*?<grade>([\d.]+)</grade>'
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
        'message_analysis': {
            'reasoning': r'<message_analysis>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<message_analysis>.*?<grade>([\d.]+)</grade>'
        },
        'pattern_matching': {
            'reasoning': r'<pattern_matching>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<pattern_matching>.*?<grade>([\d.]+)</grade>'
        },
        'output': {
            'reasoning': r'<output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)


def parse_question_six(response: str) -> dict:
    patterns = {
        'thinking': r'<thinkpad>(.*?)</thinkpad>',
        'engagement_calc': {
            'reasoning': r'<engagement_calc>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<engagement_calc>.*?<grade>([\d.]+)</grade>'
        },
        'content_analysis': {
            'reasoning': r'<content_analysis>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<content_analysis>.*?<grade>([\d.]+)</grade>'
        },
        'output': {
            'reasoning': r'<output>\s*<reasoning>(.*?)</reasoning>',
            'grade': r'<output>.*?<grade>([\d.]+)</grade>'
        },
        'final_score': r'<final_score>([\d.]+)</final_score>',
        'final_feedback': r'<final_feedback>(.*?)</final_feedback>'
    }
    return parse_response(response, patterns)
