#!/usr/bin/env python3

from time import time

start_time = time()

with open('input') as f:
    lines = f.readlines()

    polymer = lines[0].strip()
    rules = {}

    for line in lines[2:]:
        new_rule = line.strip().split(' -> ')
        rules[new_rule[0]] = new_rule[1]

print(rules)

pairs = {}

for i in range(len(polymer) - 1):
    pair = polymer[i:i+2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

for i in range(40):
    next_pairs = {}

    for pair, count in pairs.items():
        if pair in rules:
            # Get the new set of pairs that will be created
            new_pairs = (pair[0] + rules[pair], rules[pair] + pair[1])
            for new_pair in new_pairs:
                if new_pair in next_pairs:
                    next_pairs[new_pair] += count
                else:
                    next_pairs[new_pair] = count
    
    pairs = next_pairs

# Calculate the count of all the letters
letter_counts = {}

for pair, count in pairs.items():
    for letter in pair:
        if letter in letter_counts:
            letter_counts[letter] += count
        else:
            letter_counts[letter] = count

letter_counts[polymer[0]] += 1
letter_counts[polymer[-1]] += 1

# divide all the letter counts by 2
for letter, count in letter_counts.items():
    letter_counts[letter] = count // 2

max_count = max(letter_counts.values())
min_count = min(letter_counts.values())

print(max_count - min_count)

end_time = time()

print(f'{1000 * (end_time - start_time):.3f} ms')
