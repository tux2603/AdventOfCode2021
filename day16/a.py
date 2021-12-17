#!/usr/bin/env python3

# Define a bunch of classes that will be used to represent different lexer nodes
# class Node:
#     def __init__(self, node_type, value, children):
#         self.node_type = node_type
#         self.value = value
#         self.children = children

# class Lexer:
#     def __init__(self, data):
#         self.data = data
#         self.pos = 0

#     def get_next_token(self):

class Packet:
    def __init__(self, version, packet_type, value=0, children=[]):
        self.version = version
        self.packet_type = packet_type
        self.value = value
        self.children = children

    def eval(self):
        return self.version + sum(child.eval() for child in self.children)

    def __str__(self, depth=0):
        ret = '    ' * depth

        if self.packet_type == 4:
            ret += f'Literal with value {self.value}\n'
        else:
            ret += f'Operator with children:\n{"".join(child.__str__(depth=depth+1) for child in self.children)}\n'

        return ret


class Lexer:
    def __init__(self, data):
        self.data = data
        self.pos = 0
        self.root = None

    def parse(self):
        self.root = self.get_next_token()

    def get_next_token(self, depth=0):
        print(f'{"    " * depth}[Index {self.pos}] -- ', end='')
        # Get the version and node type of the next from next three chars
        version = int(self.data[self.pos:self.pos+3], 2)
        self.pos += 3

        # Get the packet type of the next three chars
        packet_type = int(self.data[self.pos:self.pos+3], 2)
        self.pos += 3

        value = 0
        children = []

        print(f'Version: {version}, Packet type: {packet_type}', end='')

        # If this is a literal value node, parse it as such
        if packet_type == 4:
            value_string = ''

            while self.data[self.pos] == '1':
                self.pos += 1

                # Add the next four chars to the value string
                value_string += self.data[self.pos:self.pos+4]
                self.pos += 4

            # Append the last chunk of the value string to the value
            value_string += self.data[self.pos+1:self.pos+5]
            self.pos += 5
            
            # Convert the value string to an integer
            value = int(value_string, 2)

            print(f', Value: {value}')

        # Else this is an operator node, parse it as such
        else:
            # The next bit will signify what sort of length value we're dealing with
            length_type = int(self.data[self.pos], 2)
            self.pos += 1

            # If the length type is 0, the next 15 bits will be the length of the children packets in bits
            if length_type == 0:
                num_bits = int(self.data[self.pos:self.pos+15], 2)
                self.pos += 15

                print(f', Length: {num_bits} bits')

                # Keep track of the startung position so we can know when to stop parsing children
                start_pos = self.pos

                # Keep parsing children until we've parsed the number of bits specified
                while self.pos - start_pos < num_bits:
                    children.append(self.get_next_token(depth=depth+1))

            # If the length type is 1, the next 11 bits will be the total number of child subpackets
            elif length_type == 1:
                num_subpackets = int(self.data[self.pos:self.pos+11], 2)
                self.pos += 11

                print(f', Length: {num_subpackets} subpackets')

                for i in range(num_subpackets):
                    children.append(self.get_next_token(depth=depth+1))

            else:
                raise Exception('Invalid length type')



        return Packet(version, packet_type, value, children)

    def eval(self):
        if self.root is None:
            return 0

        return self.root.eval()

    def __str__(self):
        if self.root is None:
            return ''

        return self.root.__str__()



# table to hold conversion from hex to binary
hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

bit_string = ''
with open('input') as f:
    for line in f:
        for c in line:
            bit_string += hex_to_bin[c]

l = Lexer(bit_string)
l.parse()
# print(l)
print(l.eval())




