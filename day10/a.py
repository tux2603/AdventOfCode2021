#!/user/bin/env python3

with open('input') as f:
    lines = f.readlines()

total_value = 0

for line in lines:
    stack = []
    first_incorrect = ''

    for c in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                first_incorrect = c
                total_value += 3
                break
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                first_incorrect = c
                total_value += 57
                break
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                first_incorrect = c
                total_value += 1197
                break
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                first_incorrect = c
                total_value += 25137
                break
    
    # if first_incorrect:
    #     print(f'{first_incorrect} was unexpected')

print(total_value)
