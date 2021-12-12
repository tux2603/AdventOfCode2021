
from pprint import pprint

with open('input') as f:
    lines = f.readlines()

    # Get the largest number in the file
    largest_x = 0
    largest_y = 0
    for line in lines:
        line = line.strip()
        start, end = line.split(' -> ')
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')

        if int(start_x) > largest_x:
            largest_x = int(start_x)
        if int(start_y) > largest_y:
            largest_y = int(start_y)
        if int(end_x) > largest_x:
            largest_x = int(end_x)
        if int(end_y) > largest_y:
            largest_y = int(end_y)

    grid = [[0 for y in range(largest_y+1)] for x in range(largest_x+1)]

    for line in lines:
        line = line.strip()
        start, end = line.split(' -> ')
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')

        # convert to ints
        start_x = int(start_x)
        start_y = int(start_y)
        end_x = int(end_x)
        end_y = int(end_y)

        # Backup tthe values for when we have to deal with diagonal lines
        start_x_backup = start_x
        start_y_backup = start_y
        end_x_backup = end_x
        end_y_backup = end_y

        # Make sure that the start coordinate is smaller than the end coordinate
        if start_x > end_x:
            start_x, end_x = end_x, start_x
        if start_y > end_y:
            start_y, end_y = end_y, start_y

        # print(f'Drawing a line from ({start_x}, {start_y}) to ({end_x}, {end_y})')

        # fill in the grid
        if start_x == end_x:
            for i in range(start_y, end_y+1):
                grid[start_x][i] += 1

        elif start_y == end_y:
            for i in range(start_x, end_x+1):
                grid[i][start_y] += 1

        else:
            # This is garunteed to be a diagonal line
            start_x = start_x_backup
            start_y = start_y_backup
            end_x = end_x_backup
            end_y = end_y_backup

            x_step = 1 if start_x < end_x else -1
            y_step = 1 if start_y < end_y else -1

            for i in range(abs(end_x - start_x) + 1):
                grid[start_x + i * x_step][start_y + i * y_step] += 1

        # pprint(grid)


# count the nnumber of elemennts in the firts grid that are greater than one
count = sum(sum(i > 1 for i in row) for row in grid)
# pprint(grid)

print(count)