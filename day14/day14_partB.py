# adventOfCode 2016 day 14, part B
# https://adventofcode.com/2016/day/14

import hashlib
import re
import sys


# This seeks a repeated character in a string
# It returns None if no character is repeated at least repeat_number times in the_str
# Otherwise, it returns the character that is repeated in the first (leftmost) instance of any character repeated repeat_number times
def seek_repeat(the_str, repeat_number):
    regex_str = r'(.)\1{' + str(repeat_number - 1) + ',}'
    rx = re.compile(regex_str)
    result = rx.search(the_str)
    if result is None:
        return None
    return the_str[result.regs[0][0]]

# Pytest testing function
def test_seek_repeat():
    # Verify that seek_repeat only returns the character from the first observed cluster
    assert seek_repeat('aaaaabbbbb', 3) == 'a'

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file {input_filename}')
with open(input_filename) as f:
    salt = f.readline().rstrip()
    print(f'This contains: {salt}\n')

append_int = 0
triple_indices_to_char = dict()
indices_valid_keys = list()

while True:
    append_str = str(append_int)
    hashed_str = salt + append_str
    for i in range(2017):
        hashed_str = hashlib.md5(hashed_str.encode()).hexdigest()

    triplet = seek_repeat(hashed_str, 3)
    if triplet:
        # quick and dirty search for any five characters in a row
        quintet = seek_repeat(hashed_str, 5)
        if quintet:
            # use triple_indices_to_char to look if it has the right five chars. in a row
            # Perform more thorough search for five instances of a character in a row that 
            # match three instances of that same character in a row in the 1000 most recent MD5 hashes
            triple_indices_to_char__indices_to_delete = set()
            for index in triple_indices_to_char.keys():
                # Below is to meet the below requirement from the spec.
                # "One of the next 1000 hashes in the stream contains that same character five times in a row"
                if index < append_int - 1000:
                    triple_indices_to_char__indices_to_delete.add(index)
                else:
                    ch = triple_indices_to_char[index]
                    if ch*5 in hashed_str:
                        indices_valid_keys.append(index)

                        if len(indices_valid_keys) > 63:
                            if min(indices_valid_keys) < min(list(triple_indices_to_char.keys())) - 1000:
                                print(f'The index that produces the 64th valid key (the answer to part B) is {sorted(indices_valid_keys)[-1]}\n')
                                print(f'The sorted list of keys is: {sorted(indices_valid_keys)}\n')
                                sys.exit('Program completed successfully')

            for index in triple_indices_to_char__indices_to_delete:
                del triple_indices_to_char[index]

        triple_indices_to_char[append_int] = triplet

    append_int += 1


