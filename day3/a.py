with open('input') as f:
    lines = f.readlines()

counts = [0] * len(lines[0].strip())

for line in lines:
    for i, c in enumerate(line):
        if c == '0':
            counts[i] -= 1
        elif c == '1':
            counts[i] += 1

gamma_str = ''.join(['1' if c > 0 else '0' for c in counts])
epsilon_str = ''.join(['1' if c < 0 else '0' for c in counts])
gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)
consumption = gamma * epsilon

print(consumption)