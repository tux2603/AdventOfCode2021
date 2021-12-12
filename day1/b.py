#!/usr/bin/env python3

# Convert all of the lines in the input file to integers
with open('input', 'r') as f:
    values = [int(line) for line in f]

# Get the three measurement windows
windows = [sum(values[i:i+3]) for i in range(len(values)-2)]

# Get the number of times thhat a window was greater than the previous window
num_greater = len([1 for i in range(len(windows)-1) if windows[i] < windows[i+1]])
print(num_greater)