#!/usr/bin/env python3

horizontal_position = 0
vertical_position = 0
aim = 0

with open('input') as f:
    for line in f:
        direction = line.split()[0]
        distance = int(line.split()[1])

        if direction == 'forward':
            horizontal_position += distance
            vertical_position += distance * aim

        elif direction == 'up':
            aim -= distance
        
        elif direction == 'down':
            aim += distance

print(horizontal_position * vertical_position)