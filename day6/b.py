fish_counts = [0 for _ in range(9)]

with open('input') as f:
    for line in f:
        numbers = [int(x) for x in line.split(',')]
        for number in numbers:
            fish_counts[number] += 1

for _ in range(256):
    # print(fish_counts)
    new_fish_counts = [0 for _ in range(9)]
    new_fish_spawned = fish_counts[0]
    for i in range(8):
        new_fish_counts[i] = fish_counts[i+1]
    new_fish_counts[8] = new_fish_spawned
    new_fish_counts[6] += new_fish_spawned
    fish_counts = new_fish_counts

print(sum(fish_counts))