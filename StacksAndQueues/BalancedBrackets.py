def balancedBrackets(string):
    bracket_pairs = {}
    bracket_pairs['('] = ')'
    bracket_pairs['['] = ']'
    bracket_pairs['{'] = '}'
    bracket_stack = []
    valid_brackets = "()[]{}"

    for char in string:
        if char not in valid_brackets:
            continue
        if char in bracket_pairs:
            bracket_stack.append(bracket_pairs[char])
        else:
            if len(bracket_stack) == 0:
                return False
            if bracket_stack[-1] != char:
                return False
            else:
                bracket_stack.pop()
    return len(bracket_stack) == 0
