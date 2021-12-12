#!/user/bin/env python3

with open('input') as f:
    lines = f.readlines()

line_values = []

for line in lines:
    stack = []
    first_incorrect = None

    for c in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                first_incorrect = c
                break
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                first_incorrect = c
                break
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                first_incorrect = c
                break
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                first_incorrect = c
                break
    
    if first_incorrect is None:
        line_value = 0
        while(stack):
            line_value *= 5
            c = stack.pop()
            if c == '(':
                line_value += 1
            elif c == '[':
                line_value += 2
            elif c == '{':
                line_value += 3
            elif c == '<':
                line_value += 4
        line_values.append(line_value)

line_values.sort()

print(line_values[len(line_values) // 2])

