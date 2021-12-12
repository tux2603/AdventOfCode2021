from pprint import pprint

class Node:
    def __init__(self, name):
        self.neighbors = []
        self.name = name
        self.cave_type = name.upper() == name
        self.visit_count = 0

    def __str__(self):
        return f'Node {self.name} with neighbors {", ".join(neighbor.name for neighbor in self.neighbors)}'

def get_num_paths(current_node, depth=0, path=[], small_cave=False):
    # print(f'{depth * "  "}Visiting {current_node.name} (Visit count {current_node.visit_count}) -- [{", ".join(i.name for i in path)}], a small cave {"has" if small_cave else "has not"} been visited twice')

    # If the name of this node is "end", then we're done with recursion
    if current_node.name == 'end':
        return 1
    
    num_paths = 0
    for neighbor in current_node.neighbors:
        if neighbor.visit_count < (1 if small_cave else 2) or neighbor.cave_type:
            neighbor.visit_count += 1
            old_small_cave = small_cave
            if not neighbor.cave_type and neighbor.visit_count == 2:
                small_cave = True
            path.append(neighbor)
            num_paths += get_num_paths(neighbor, depth+1, path, small_cave)
            small_cave = old_small_cave
            path.pop()
            neighbor.visit_count -= 1
    return num_paths
    

if __name__ == '__main__':
    nodes = {}
    with open('input') as f:
        for line in f:
            a, b = line.strip().split('-')

            if a not in nodes:
                nodes[a] = Node(a)
            if b not in nodes:
                nodes[b] = Node(b)

            nodes[a].neighbors.append(nodes[b])
            nodes[b].neighbors.append(nodes[a])

    nodes['start'].visit_count = 2
    num_paths = get_num_paths(nodes['start'], path=[nodes['start']])
    print(f'Number of paths: {num_paths}')

    # for node in nodes.values():
    #     print(node)

            