# adventOfCode 2016 day 15
# https://adventofcode.com/2016/day/15


import sys

# disc number, initial position, and number of positions are in a dict in each element in list disc_structure
disc_structure = list()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip().split(' ')

        # Assert that all input data must be the initial conditions (at time zero)
        assert in_string[6] == 'time=0,'

        disc_structure.append({
            'disc_number':int(in_string[1][1:]),
            'position_count': int(in_string[3]),
            'initial_position': int(in_string[-1][:-1])
            })

time_drop = 0
while True:
    for disc in disc_structure:
        time = time_drop + disc['disc_number']
        if 0 != (disc['initial_position'] + time) % disc['position_count']:
            break
        if disc == disc_structure[-1]:
            print(f'Answer found: {time_drop}\n')
            sys.exit('Program exited successfully.')
    time_drop += 1


