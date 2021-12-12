#!!/usr/bin/env python3

floor = []
with open('input') as f:
    for line in f:
        line = line.strip()
        floor.append([int(i) for i in line])

low_points = []

# Find all the points in the floor that are lower than the adjacent points
for i in range(len(floor)):
    for j in range(len(floor[i])):
        is_lower = True

        if i > 0 and floor[i-1][j] <= floor[i][j]:
            is_lower = False

        if i < len(floor)-1 and floor[i+1][j] <= floor[i][j]:
            is_lower = False
        
        if j > 0 and floor[i][j-1] <= floor[i][j]:
            is_lower = False

        if j < len(floor[i])-1 and floor[i][j+1] <= floor[i][j]:
            is_lower = False

        if is_lower:
            low_points.append((i,j))

# print(low_points)

# print([floor[i][j] for i,j in low_points])

print(sum(floor[i][j] + 1 for i,j in low_points))