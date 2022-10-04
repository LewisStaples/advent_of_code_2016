# adventOfCode 2016 day 17
# https://adventofcode.com/2016/day/17


import sys
import hashlib


# Reading input from the input file
input_filename='input_sample1.txt'
with open(input_filename) as f:
    passcode_str = f.readline().rstrip()
print(f'\nUsing input file: {input_filename}')
print(f'and this file contains {passcode_str}')   
 
# Collection that lists all points on the board:
permissible_points = set()
for i in range(4):
    for j in range(4):
        permissible_points.add((i,j))

current_paths = {'':(0,0)}
destination = (3,3)

next_paths = {}
directions = {'U':(0,-1), 'D':(0,1), 'L':(-1,0), 'R':(1,0)}
while True:
    for path, point in current_paths.items():
        hash_str = hashlib.md5((passcode_str + path).encode()).hexdigest()
        for i, (direction, step) in enumerate(directions.items()):
            # check if next_point is outside the grid
            next_point = (point[0] + step[0], point[1] + step[1])
            if next_point not in permissible_points:
                continue
            # check if the door is open in this direction
            if hash_str[i] not in ['b', 'c', 'd', 'e', 'f']:
                continue
            # both checks above confirm that next_point can be visited next
            new_path = path + direction
            next_paths[new_path] = next_point
            if next_point == destination:
                print(f'The shortest path is: {new_path}')
                sys.exit('\nProgram successfully completed\n')

    if len(next_paths) == 0:
        break
    current_paths = next_paths
    next_paths = {}

