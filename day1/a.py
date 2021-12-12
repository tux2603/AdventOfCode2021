#!/usr/bin/env python3

old_value = int(input())
num_greater = 0

try:
    while True:
        new_value = int(input())
        if new_value > old_value:
            num_greater += 1
        old_value = new_value
except EOFError:
    print(num_greater)
    
        