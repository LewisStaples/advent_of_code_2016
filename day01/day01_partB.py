# adventOfCode 2016 day 1, part B
# https://adventofcode.com/2016/day/1


import math
import sys

status = {
    'vertical': 0,
    'horizontal': 0,
    'orientation': 0
}

def degrees_to_unit_vector(degrees):
    trig_calculation = [
        round(math.sin(degrees * math.pi/180)) ,
        round(math.cos(degrees * math.pi/180))
        ]
    
    return (
        'vertical' if trig_calculation.index(0) == 0 else 'horizontal',
        sum(trig_calculation)
    )

# Read input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()


def add_points(all_points_visited, magnitude, status, unit_vector):
    for unused_variable in range(1, magnitude+1):
        status[unit_vector[0]] += unit_vector[1]
        if (status['horizontal'], status['vertical']) in all_points_visited:
            print('The answer to part B is: ', end='')
            print( abs(status['horizontal']) + abs(status['vertical']) )
            print()
            sys.exit('Program Ending Successfully ...\n')
        all_points_visited.add( (status['horizontal'], status['vertical']) )

all_points_visited = {(0,0)}


input_list = in_string.split(', ')
for segment in input_list:
    if segment[0] == 'L':
        status['orientation'] = (status['orientation'] - 90) % 360
    elif segment[0] == 'R':
        status['orientation'] = (status['orientation'] + 90) % 360

    magnitude = int(segment[1:])
    unit_vector = degrees_to_unit_vector(status['orientation'])
    add_points(all_points_visited, magnitude, status, unit_vector)

