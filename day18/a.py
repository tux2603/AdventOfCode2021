#!/usr/bin/env python
import re

def compute_magnitude(shellfish):
    if type(shellfish) is int:
        return shellfish
    else:
        return 3 * compute_magnitude(shellfish[0]) + 2 * compute_magnitude(shellfish[1])

numbers = []
with open('input') as f:
    for line in f:
        numbers.append(line.strip())

print('\n'.join(numbers))
print('----')

while len(numbers) > 1:
    first = numbers.pop(0)
    numbers[0] = f'[{first},{numbers[0]}]'
    print('\n'.join(numbers))
    print('----')

    while True:

        # Check for any pairs that are more than four nodes deep
        depth = 0
        pair_start = -1
        pair_end = -1
        for i, c in enumerate(numbers[0]):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            if depth > 4 and pair_start == -1:
                pair_start = i
                action_found = True
            elif pair_start > -1 and depth <= 4:
                pair_end = i+1
                break

        if pair_start > -1 and pair_end > -1:
            before = numbers[0][:pair_start]
            pair = numbers[0][pair_start:pair_end]
            after = numbers[0][pair_end:]

            left_value = eval(pair)[0]
            right_value = eval(pair)[1]

            before_value = "n/a"
            after_value = "n/a"

            # Find the last digit in before
            before_digits = re.findall(r'\d+', before)
            if len(before_digits) > 0:
                before_value = int(before_digits[-1])
                before_value_index = before.rfind(before_digits[-1])

                # replace the substring containing before_value with the sum of left_value and before_value
                before = before[:before_value_index] + str(left_value + before_value) + before[before_value_index + len(before_digits[-1]):]


            # Find the first digit in after
            after_digits = re.findall(r'\d+', after)
            if len(after_digits) > 0:
                after_value = int(after_digits[0])
                after_value_index = after.find(after_digits[0])

                # replace the substring containing after_value with the sum of right_value and after_value
                after = after[:after_value_index] + str(right_value + after_value) + after[after_value_index + len(after_digits[0]):]
            

            print(f'{before} (last number {before_value}) {left_value} {right_value} (first number {after_value}) {after}')
            numbers[0] = before + '0' + after
            continue

        # Check to see if there are any values over 10
        # Use regex to find the index of the first number with more than one digit
        large_number  = re.search(r'\d{2,}', numbers[0])

        if large_number:
            large_number_start = large_number.start()
            large_number_end = large_number.end()

            # print with the large number highlighted
            print(f'{numbers[0][:large_number_start]}\033[1m{numbers[0][large_number_start:large_number_end]}\033[0m{numbers[0][large_number_end:]}')

            number = int(numbers[0][large_number_start:large_number_end])
            half_round_down = number // 2
            half_round_up = number // 2 + (1 if number % 2 == 1 else 0)

            # replace the large number with [half_round_down, half_round_up]
            numbers[0] = numbers[0][:large_number_start] + f'[{half_round_down},{half_round_up}]' + numbers[0][large_number_end:]

            continue
        
        break

print(numbers[0])
print(compute_magnitude(eval(numbers[0])))



