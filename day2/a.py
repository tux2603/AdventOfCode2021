#!/usr/bin/env python3

vertical_position = 0
horizontal_position = 0

with open('input') as f:
    for line in f:
        direction = line.split()[0]
        distance = int(line.split()[1])

        if direction == 'forward':
            vertical_position += distance
        elif direction == 'up':
            horizontal_position -= distance
        elif direction == 'down':
            horizontal_position += distance

print(vertical_position * horizontal_position)