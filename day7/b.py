with open('input') as f:
    line = f.readlines()[0]
    crab_locations = [int(i) for i in line.split(',')]
    min_crab_location = min(crab_locations)
    max_crab_location = max(crab_locations)

min_cost = -1

for i in range(min_crab_location, max_crab_location + 1):
    cost = sum(int(0.5 * abs(x - i) * (abs(x - i) + 1)) for x in crab_locations)
    if min_cost == -1 or cost < min_cost:
        min_cost = cost

print(min_cost)
    