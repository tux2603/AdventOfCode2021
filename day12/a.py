from pprint import pprint

class Node:
    def __init__(self, name):
        self.neighbors = []
        self.name = name
        self.cave_type = name.upper() == name
        self.visited = False

    def __str__(self):
        return f'Node {self.name} with neighbors {", ".join(neighbor.name for neighbor in self.neighbors)}'

def get_num_paths(current_node, depth=0, path=[]):
    # print(f'{depth * "  "}Visiting {current_node.name} -- [{", ".join(i.name for i in path)}]')

    # If the name of this node is "end", then we're done with recursion
    if current_node.name == 'end':
        return 1
    
    num_paths = 0
    for neighbor in current_node.neighbors:
        if not neighbor.visited or neighbor.cave_type:
            neighbor.visited = True
            path.append(neighbor)
            num_paths += get_num_paths(neighbor, depth+1, path)
            path.pop()
            neighbor.visited = False
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

    nodes['start'].visited = True
    num_paths = get_num_paths(nodes['start'], path=[nodes['start']])
    print(f'Number of paths: {num_paths}')

    # for node in nodes.values():
    #     print(node)

            