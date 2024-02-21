import re


TOKENS = {
    'identifier': r'[a-zA-Z_]\w*',  # Matches identifiers
    'keyword': r'int|float|char|double',  # Matches keywords
    'separator': r'[ ; , () {} \[\]]',  # Matches separators (comma, semicolon, and brackets)
    'operator': r'[+\-*/=]',  # Matches operators
    'whitespace': r'\s+',  # Matches whitespace
    'special_character': r'[^a-zA-Z \s]',  # Matches special characters
    'numbers': r'[0-9]'  # Matches numbers
}

# Symbol table
symbol_table = {}

def lexical_analyzer(statement):
    tokens = []
    count=0
    while statement:
        matched = False
        for token_type, pattern in TOKENS.items():
            match = re.match(pattern, statement)
            if match:
                if token_type == 'identifier':
                    identifier = match.group(0)
                    if identifier not in symbol_table:
                        count=count+1
                        symbol_table[identifier] = count
                tokens.append((token_type, match.group(0)))
                statement = statement[match.end():]
                matched = True
                break
        if not matched:
            print("Lexical Error: Unrecognized token at: " + statement[0])
            return None
    return tokens

def main():
    statement = input("Enter declaration or definition statement: ")
    tokens = lexical_analyzer(statement)
    if tokens:
        print("Tokens:", tokens)
        print("Symbol Table:", symbol_table)

if __name__ == "__main__":
    main()
