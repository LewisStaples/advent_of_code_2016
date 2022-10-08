# adventOfCode 2016 day 20
# https://adventofcode.com/2016/day/20


import sys


all_invalid_numbers = dict()

input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        [lower, upper] = [int(x) for x in in_string.split('-')]
        all_invalid_numbers[lower] = upper

next_lower = 0
for key in sorted(all_invalid_numbers.keys()):
    if next_lower < key:
        # answer found
        print(f'The answer to part A is {next_lower}\n')
        sys.exit('Program successfully completed\n')
    else:
        next_lower = max(next_lower, all_invalid_numbers[key]+1)

