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