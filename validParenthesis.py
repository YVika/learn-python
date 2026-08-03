def validParenthesis(s: str) -> bool:
    stack = []

    if len(stack) // 2 == 1:
        return False

    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
            continue
        if not bool(stack):
            return False
        if (
            char == ")"
            and stack[-1] == "("
            or char == "}"
            and stack[-1] == "{"
            or char == "]"
            and stack[-1] == "["
        ):
            stack.pop()
        else:
            return False

    return not bool(stack)


print(validParenthesis("({[])"))
