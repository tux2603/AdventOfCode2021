#!/usr/bin/env python3
import re

with open('input') as f:
    lines = f.readlines()

    polymer = lines[0].strip()
    rules= []

    for line in lines[2:]:
        new_rule = line.strip().split(' -> ')
        rules.append(new_rule)

print(rules)

for _ in range(10):
    insertions = []
    for rule in rules:
        if rule[0] in polymer:
            last_index = 0
            while True:
                # get the first index of the rule[0] and the last index of the rule[0]
                first_index = polymer.find(rule[0], last_index)
                if first_index == -1:
                    break
                insertions.append((first_index + 1, rule[1]))
                last_index = first_index + 1
            # find all occurrences of rule[0] in polymer
            # indices = [m.start() for m in re.finditer(rule[0], polymer)]
            # insertions.extend([(i + 1, rule[1]) for i in indices])
            # append the index and char
            # insertions.append((polymer.index(rule[0])+1, rule[1]))
            # break

    # sort the insertions by the first index
    insertions.sort(key=lambda x: x[0])

    for i, insertion in enumerate(insertions):
        polymer = polymer[:insertion[0] + i] + insertion[1] + polymer[insertion[0] + i:]

    # print(polymer)

# Get the counts of each letter
counts = {}
for char in polymer:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

# Getthe max and min count
max_count = max(counts.values())
min_count = min(counts.values())

print (max_count)
print (min_count)

print(max_count - min_count) 