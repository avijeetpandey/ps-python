def validParenthesis(str):
    stack = []
    for char in str:
        if isOpening(char):
            stack.append(char)
        elif isClosing(char):
            if not stack or not isMatching(stack.pop(), char):
                return False
    return not stack

def isOpening(ch):
    return ch == '[' or ch == '{' or ch == '('

def isClosing(ch):
    return ch == ']' or ch == '}' or ch == ')'

def isMatching(opening, closing):
    return (opening == '[' and closing == ']') or (opening == '{' and closing == '}') or (opening == '(' and closing == ')')