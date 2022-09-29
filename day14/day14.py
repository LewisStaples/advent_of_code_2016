# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??

import hashlib
import re


def seek_repeat(the_str, repeat_number):
    regex_str = r'(.)\1{' + str(repeat_number - 1) + ',}'
    rx = re.compile(regex_str)
    result = rx.search(the_str)
    if result is None:
        return None
    return the_str[result.regs[0][0]]


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file {input_filename}')
with open(input_filename) as f:
    salt = f.readline().rstrip()
    print(f'This contains: {salt}\n')

append_int = 0
indices_triples = dict()


while True:
    append_str = str(append_int)
    combined_str = salt + append_str
    hashed_str = hashlib.md5(combined_str.encode()).hexdigest()

    # print(append_int)


    triplet = seek_repeat(hashed_str, 3)
    if triplet:
        indices_triples[append_int] = triplet
        # print(f'{combined_str}: {triplet} & {hashed_str}')

        # quick and dirty search for any five characters in a row
        quintet = seek_repeat(hashed_str, 5)
        if quintet:
            pass  # to be implemented .... use indices_triples to look if it has the right five chars. in a row

    # when complete then call below ....
    if append_int > 100:
        break
    
    append_int += 1

print()
