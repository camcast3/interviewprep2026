def valid_parenthesis_expression(string: str) -> bool:
    parenthesis_mapping = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in string:

        if char in parenthesis_mapping:
            stack.append(char)

        else:
            if stack and parenthesis_mapping[stack[-1]] == char:
                stack.pop()

            else:
                return False

    return True
