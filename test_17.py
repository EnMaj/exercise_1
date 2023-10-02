def prec(c):
    if c == '*' or c == '/':
        return 3
    if c == '+' or c == '-':
        return 4
    return 100

def infixToPostfix(infix):
    if not infix or not len(infix):
        return True
    s = []
    postfix = ''
    for c in infix:
        if c == '(':
            s.append(c)
        elif c == ')':
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()
        elif c.isdigit():
            postfix += c
        else:
            while s and prec(c) >= prec(s[-1]):
                postfix += s.pop()
            s.append(c)
    while s:
        postfix += s.pop()
    return postfix

def evalPostfix(exp):
    if not exp:
        exit(-1)
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            x = stack.pop()
            y = stack.pop()
            if ch == '+':
                stack.append(y + x)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(y * x)
            elif ch == '/':
                stack.append(y // x)
    return stack.pop()



infix = input()
postfix = infixToPostfix(infix)
print(evalPostfix(postfix))