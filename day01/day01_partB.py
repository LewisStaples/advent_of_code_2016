# adventOfCode 2016 day 1, part B
# https://adventofcode.com/2016/day/1

import copy

status = {
    'vertical': 0,
    'horizontal': 0,
    'orientation': 0
}

# starting_status = copy.deepcopy(status)
# Reading input from the input file
input_filename='input_sample2.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()


def add_points(all_points_visited, magnitude, status):
    # position = [status['horizontal'], status['vertical']]
    for magnitude_partial in range(1, magnitude+1):
        all_points_visited.add( (status['horizontal'], status['vertical']) )

all_points_visited = {(0,0)}

# Parsing input file   
input_list = in_string.split(', ')
for segment in input_list:
    if segment[0] == 'L':
        status['orientation'] = (status['orientation'] - 90) % 360
    elif segment[0] == 'R':
        status['orientation'] = (status['orientation'] + 90) % 360

    magnitude = int(segment[1:])
    add_points(all_points_visited, magnitude, status)
    if status['orientation'] == 0:
        status['vertical'] += magnitude
    elif status['orientation'] == 90:
        status['horizontal'] += magnitude
    elif status['orientation'] == 180:
        status['vertical'] -= magnitude
    elif status['orientation'] == 270:
        status['horizontal'] -= magnitude
    
    

# answer_A = abs(status['horizontal']) + abs(status['vertical'])
# print(f'The answer to part A is {answer_A}\n')

