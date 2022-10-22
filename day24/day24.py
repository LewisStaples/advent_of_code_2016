# adventOfCode 2016 day 24
# https://adventofcode.com/2016/day/24


import numpy as np
import itertools


# Reading input from the input file
# Use this to populate duct_positions (this excludes '#')
duct_positions = dict()
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for i, in_string in enumerate(f):
        in_string = in_string.rstrip()
        for j, ch in enumerate(in_string):
            if ch != '#':
                duct_positions[(i,j)] = ch


# Calculate the least distance between all pairs of numbered points
least_dist_betw_numbered_pts = dict()
for coords, ch in duct_positions.items():
    if ch in ['#','.']:
        continue
    stepcount_now = 0
    distance_mapping_for_this_position = {coords:stepcount_now}

    while True:
        latest_positions = []
        for position, position_stepcount in distance_mapping_for_this_position.items():
            if position_stepcount != stepcount_now:
                continue
            latest_positions.append(position)
        # Stop when there are no additional spaces to move to
        if len(latest_positions) == 0:
            break
        stepcount_now += 1
        for position in latest_positions:
            for delta in [(0,-1), (0,1), (-1,0), (1,0)]:
                new_position = tuple(np.add(position, delta))
                if new_position not in duct_positions:
                    continue
                if new_position not in distance_mapping_for_this_position:
                    distance_mapping_for_this_position[new_position] = stepcount_now
                    new_ch = duct_positions[new_position]
                    if new_ch.isdigit():
                        new_pairing = tuple(sorted([ch, new_ch]))
                        if new_pairing not in least_dist_betw_numbered_pts:
                            least_dist_betw_numbered_pts[new_pairing] = stepcount_now


# Traverse all permutations of numbered positions that can be 
# visited and calculate the distances of each of them.
# The final answer is the least distance of all of these paths.
number_labels = list(duct_positions.values())
number_labels = sorted(list(filter(lambda x: x != '.', number_labels)))
number_labels.remove('0')

min_stepcount = float('inf')
for sequence in itertools.permutations(number_labels):
    starting_point = '0'
    total = 0
    for i in range(len(sequence)):
        pair = tuple(sorted([starting_point, sequence[i]]))
        total += least_dist_betw_numbered_pts[pair]
        starting_point = sequence[i]
    min_stepcount = min(min_stepcount, total)

print(f'\nThe answer is {min_stepcount}\n')



