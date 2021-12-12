with open('input') as f:
    lines = f.readlines()

# copy the lines to to new lists
lines = [line.strip() for line in lines]

oxygen_lines = lines.copy()
oxygen_counts = [0] * len(lines[0].strip())

for i in range(len(lines[0])):
    # recompute the oxygen counts
    count = 0
    for line in oxygen_lines:
        if line[i] == '1':
            count += 1
        elif line[i] == '0':
            count -= 1
    
    if count >= 0:
        oxygen_lines = [line for line in oxygen_lines if line[i] == '1']
    
    elif count < 0:
        oxygen_lines = [line for line in oxygen_lines if line[i] == '0']

    if len(oxygen_lines) == 1:
        break



co2_lines = lines.copy()
co2_counts = [0] * len(lines[0].strip())

for i in range(len(lines[0])):
    # recompute the co2 counts
    count = 0
    for line in co2_lines:
        if line[i] == '1':
            count += 1
        elif line[i] == '0':
            count -= 1

    if count >= 0:
        co2_lines = [line for line in co2_lines if line[i] == '0']
    
    elif count < 0:
        co2_lines = [line for line in co2_lines if line[i] == '1']

    if len(co2_lines) == 1:
        break

# Convert the binary strings to ints
oxygen_lines = [int(line, 2) for line in oxygen_lines]
co2_lines = [int(line, 2) for line in co2_lines]



print(oxygen_lines[0] * co2_lines[0])

