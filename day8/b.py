#!/usr/bin/env python3  
import itertools
from numba import jit

# The patterns of digits that will be on and off in the seven segment display
letters = 'abcdefg'

letter_patterns = {
    'a': '1011011111',
    'b': '1000111011',
    'c': '1111100111',
    'd': '0011111011',
    'e': '1010001010',
    'f': '1101111111',
    'g': '1011011011'
}


permutations = list(itertools.permutations(letters))
number_patterns = []
number_strings = {}

for i in range(10):
    number_patterns.append(''.join([letter_patterns[letter][i] for letter in letters]))

for i in range(10):
    number_strings[''.join([letter for letter in letters if letter_patterns[letter][i] == '1'])] = str(i)

print(number_strings)
print(number_strings['cf'])

# @jit
def decode_line(line):
    permutations = list(itertools.permutations(letters))
    left_side, right_side = line.split('|')[0], line.split('|')[1]
    inputs = left_side.split()
    digits = right_side.split()
    mapping = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
    }


    # Filter out the non-unique elements from inputs
    inputs = list(set(inputs))

    # Iterate over every possible permutation of the letters
    for permutation in permutations:
        # Create the new mapping
        for i, letter in enumerate(permutation):
            mapping[letters[i]] = letter

        # Create a list of observed number patterns
        observed_number_patterns = []

        # print(inputs)

        for input_string in inputs:
            observed_number_patterns.append('')
            # TODO: What is going on here?
            for letter in letters:
                if mapping[letter] in input_string:
                    observed_number_patterns[-1] += '1'
                else:
                    observed_number_patterns[-1] += '0'

        # print(observed_number_patterns)

        # Check to see that all items in the observed patterns are in the number patterns and vice versa
        missing_values = False
        for number_pattern in number_patterns:
            if number_pattern not in observed_number_patterns:
                missing_values = True
                break

        for number_pattern in observed_number_patterns:
            if number_pattern not in number_patterns:
                missing_values = True
                break

        if not missing_values:
            # Reverse the mapping to make things easier
            mapping = {v: k for k, v in mapping.items()}

            translated_outputs = [''.join(sorted([mapping[letter] for letter in digit])) for digit in digits]
            # print(mapping)
            # print(translated_outputs)
            value = int(''.join([number_strings[i] for i in translated_outputs]))
            # print(value)
            return value

        

with open('input') as f:
    total = 0
    for line in f:
        total += decode_line(line)    
    print(total)