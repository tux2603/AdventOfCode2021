#!/usr/bin/env python3

def print_board(board):
    for row in board:
        print ("".join((str(i) if i != 0 else '\033[1m0\033[0m') for i in row))

with open('input') as f:
    cells = [[int(c) for c in line.strip()] for line in f]

num_cells = len(cells) * len(cells[0])

i = 0
while True:
    i += 1
    flashes = 0
    # Add one to all of the cells
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            cells[x][y] += 1

    # Any cells that are greater than nine add one to flash count and increae all neighbors by one
    new_cells_found = True
    cells_triggered = set()

    while new_cells_found:
        new_cells_found = False
        for x in range(len(cells)):
            for y in range(len(cells[x])):
                if cells[x][y] > 9 and (x, y) not in cells_triggered:

                    new_cells_found = True
                    flashes += 1
                    cells_triggered.add((x, y))

                    for x_offset in range(-1, 2):
                        for y_offset in range(-1, 2):
                            if x_offset == 0 and y_offset == 0:
                                continue
                            if x + x_offset < 0 or x + x_offset >= len(cells):
                                continue
                            if y + y_offset < 0 or y + y_offset >= len(cells[x]):
                                continue
                            cells[x + x_offset][y + y_offset] += 1

    # Any cells greater than or equal to nine get reset
    for x in range(len(cells)):
        for y in range(len(cells[0])):
            if cells[x][y] > 9:
                cells[x][y] = 0

    if num_cells == flashes:
        print(i)
        break

#     # print(f'{i}: {flashes}')
#     # print_board(cells)
#     # print()

# print(flashes)
