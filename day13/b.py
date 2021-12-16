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


# Do the folds
for fold in folds:
    if fold[0] == 'x':
        for dot in dots:
            if dot[0] > fold[1]:
                dot[0] = 2 * fold[1] - dot[0]

    if fold[0] == 'y':
        for dot in dots:
            if dot[1] > fold[1]:
                dot[1] = 2 * fold[1] - dot[1]

# convert all of the points to tuples and remove duplicates
dots = [(x, y) for x, y in dots]
dot_set = set(dots)
dots = list(dot_set)

# get the maximum x and y
max_x = max(dots, key=lambda x: x[0])[0]
max_y = max(dots, key=lambda x: x[1])[1]

# print all the dots, '.' for no dots, '#' for dots
for y in range(max_y + 1):
        print(''.join(['#' if (x, y) in dots else '.' for x in range(max_x + 1)]))