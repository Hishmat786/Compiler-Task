import re

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

def lex(code):
    tokens = []
    line_number = 1
    while code:
        match = re.match(r"^\s+", code)
        if match:
            code = code[match.end():]  # Skip whitespace
        elif match := re.match(r"^(\d+)", code):
            tokens.append(Token("INTEGER", int(match.group(1)), line_number))
            code = code[match.end():]
        elif match := re.match(r"^([a-zA-Z][a-zA-Z0-9_]*)$", code):
            tokens.append(Token("IDENTIFIER", match.group(1), line_number))
            code = code[match.end():]
        elif match := re.match(r"^(\+|-|\*|/|=|<|>|!|&&|\|\|)", code):
            tokens.append(Token("OPERATOR", match.group(1), line_number))
            code = code[match.end():]
        elif match := re.match(r"^;|\(|\)|\{|\}|\[|\]", code):
            tokens.append(Token("PUNCTUATION", match.group(1), line_number))
            code = code[match.end():]
        else:
            raise ValueError(f"Unexpected character: {code[0]} on line {line_number}")
        line_number += 1
    return tokens

# Example usage
code = """
int position = initial + rate * 60;
"""

tokens = lex(code)

for token in tokens:
    print(f"{token.type}({token.value})")
