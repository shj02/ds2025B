def check_parentheses(expression : str) -> bool: #type hint
    stack = []
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("(2+3)")) #True
print(check_parentheses("(2+(3+9))")) #True
print(check_parentheses("(2+(3+9)")) #False 스택에 여는 소괄호가 하나 남아있음
print(check_parentheses(")2+(3+9)(")) #False