#!/usr/bin/env python3

with open('input') as f:
    dots = []
    folds = []

    reading_dots = True

    for line in f:
        if line == '\n':
            reading_dots = False
            continue
    
        line = line.strip()
        if reading_dots:
            dots.append([int(i) for i in line.split(',')])

        else:
            folds.append(line.split()[-1].split('='))
            folds[-1][1] = int(folds[-1][1])


# print(dots)
# print(folds)

# Do the first fold
if folds[0][0] == 'x':
    for dot in dots:
        if dot[0] > folds[0][1]:
            dot[0] = 2 * folds[0][1] - dot[0]

if folds[0][0] == 'y':
    for dot in dots:
        if dot[1] > folds[0][1]:
            dot[1] = 2 * folds[0][1] - dot[1]

# convert all of the points to tuples and remove duplicates
dots = [(x, y) for x, y in dots]
dot_set = set(dots)
print(len(dot_set))