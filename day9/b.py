#!/usr/bin/env python3

from functools import reduce

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

# print(sum(floor[i][j] + 1 for i,j in low_points))

largest_basins = [0, 0, 0]

for low_point in low_points:
    start_x, start_y = low_point
    neighbors = []
    visited = [(start_x, start_y)]
    basin_size = 1
    if start_x > 0 and floor[start_x - 1][start_y] != 9:
        neighbors.append((start_x - 1, start_y))
    if start_x < len(floor) - 1 and floor[start_x + 1][start_y] != 9:
        neighbors.append((start_x + 1, start_y))
    if start_y > 0 and floor[start_x][start_y - 1] != 9:
        neighbors.append((start_x, start_y - 1))
    if start_y < len(floor[start_x]) - 1 and floor[start_x][start_y + 1] != 9:
        neighbors.append((start_x, start_y + 1))

    while neighbors:
        x, y = neighbors.pop()
        # print(f'Visiting {x}, {y}')
        visited.append((x, y))
        # print(visited)
        if x > 0 and floor[x - 1][y] != 9 and (x - 1, y) not in (*visited, *neighbors):
            neighbors.append((x - 1, y))
        if x < len(floor) - 1 and floor[x + 1][y] != 9 and (x + 1, y) not in (*visited, *neighbors):
            neighbors.append((x + 1, y))
        if y > 0 and floor[x][y - 1] != 9 and (x, y - 1) not in (*visited, *neighbors):
            neighbors.append((x, y - 1))
        if y < len(floor[x]) - 1 and floor[x][y + 1] != 9 and (x, y + 1) not in (*visited, *neighbors):
            neighbors.append((x, y + 1))
        basin_size += 1

    # print(f'Basin at ({x}, {y}) has size {basin_size}')
    
    largest_basins.append(basin_size)
    largest_basins.sort()
    largest_basins = largest_basins[-3:]

print(reduce(lambda x, y: x * y, largest_basins))


        
