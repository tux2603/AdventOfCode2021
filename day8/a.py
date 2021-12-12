count = 0
with open('input') as f:
    for line in f:
        right_side = line.split('|')[1]
        outputs = right_side.split()

        for output in outputs:
            if len(output) in (2, 3, 4, 7):
                count += 1

print(count)