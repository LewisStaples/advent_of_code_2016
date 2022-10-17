# adventOfCode 2016 day 22
# https://adventofcode.com/2016/day/22

# ANALYSIS OF SITUATION:
#
# Show three types of nodes:  
# the one zero-used amount node, 
# the few nodes with very large used amounts,
# for the rest, show their smallest size and largest used amounts
#
# This shows that there is one zero used node.
# There are six nodes with used amounts that are almost 500 and their sizes not much larger
# (they can't ever be swapped any any other node)
# The other nodes (not counting the seven above) has used amounts between 64 and 73
# and these can only be swapped with the zero use node.

from collections import namedtuple
from itertools import count
import numpy as np

node_list = []
count_valid_pairs = 0
Node = namedtuple('Node', ['Filesystem', 'Size', 'Used', 'Avail', 'UsePct'])
max_x = 0
max_y = 0
zero_node_coords = None

def remove_unit(in_string):
    if not in_string.isdigit():
        if in_string[:-1].isdigit():
            return int(in_string[:-1])
    return in_string

def get_x_coordinate(in_string):
    i0 = in_string.find('-x')
    i1 = in_string.find('-y')
    return int(in_string[i0+2:i1])

def get_y_coordinate(in_string):
    i = in_string.find('-y')
    return int(in_string[i+2:])


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        if line_num < 2:
            continue
        in_string = in_string.rstrip()
        in_fields = in_string.split()
        in_fields = [remove_unit(x) for x in in_fields]
        max_x = max(max_x, get_x_coordinate(in_fields[0]))
        max_y = max(max_y, get_y_coordinate(in_fields[0]))
        node_list.append(Node(*in_fields))

largest_size = 0
smallest_size = float('inf')
largest_used = 0
smallest_used = float('inf')

large_nodes = set()
large_nodes_coords = set()
for i, node in enumerate(node_list):
    if node.Used > 100:
        large_nodes.add(node)
        large_nodes_coords.add((get_x_coordinate(node.Filesystem),get_y_coordinate(node.Filesystem)))
        continue
    if node.Used == 0:
        zero_node_coords = (get_x_coordinate(node.Filesystem),get_y_coordinate(node.Filesystem))
        print('Used is zero at node: ', end='')
        print(node)
        print(f'This is at coordinates:{zero_node_coords}')

    else:
        smallest_used = min(smallest_used, node.Used)
        largest_size = max(largest_size, node.Size)

    smallest_size = min(smallest_size, node.Size)
    largest_used = max(largest_used, node.Used)
del i, node

print()
for large_node in large_nodes:
    print('Large usage node is: ', end='')
    print(large_node, end='')
    print(f', at coordinates: ({get_x_coordinate(large_node.Filesystem)},{get_y_coordinate(large_node.Filesystem)})')
    
print(f'\nLargest size found in any node (except for those listed as large above): {largest_size}')
print(f'Smallest size found in any node: {smallest_size}')
print(f'Largest used found in any node (except for those listed as large above): {largest_used}')
print(f'Smallest used found in any node (except for the zero used node above): {smallest_used}\n')
target_node_coords = (max_x, 0)
print(f'The "target" node is at coordinates: {target_node_coords}\n')

# clean up variables
del count_valid_pairs, f, in_fields, in_string, input_filename
del large_node, largest_size, largest_used, line_num, large_nodes
del smallest_size, smallest_used


# COUNTING STEPS

# Count steps to get the zero-node adjacent to the target
step_count = 0
zero_node_history = dict()
zero_node_history[zero_node_coords] = step_count
while True:
    # Construct a list of coordinates for the zero-nodes' latest spread
    list_latest_zero_nodes = []
    for node_coords, node_count in zero_node_history.items():
        if node_count == step_count:
            list_latest_zero_nodes.append(node_coords)
    
    step_count += 1
    for node in list_latest_zero_nodes:
        for del_node in [(-1,0),(0,-1),(0,1),(1,0)]:
            new_node = tuple(np.add(node, del_node))
            # Verify that x and y values aren't outside of the grid's limits
            if True in [new_node[0] < 0, new_node[1]< 0, new_node[0] > max_x, new_node[1] > max_y]:
                continue
            # Verify that new_node isn't very, very large
            if new_node in large_nodes_coords:
                continue
            # Verify that new_node isn't already in zero_node_history
            if new_node in zero_node_history:
                continue
            # Verify that new_node hasn't displaced the target
            # (because I don't want to discover a path to get adjacent
            # to the target node that goes through the target itself!)
            if new_node == target_node_coords:
                continue

            zero_node_history[new_node] = step_count


    # Stop when number of steps to all locations adjacent to the target have been discovered
    if (max_x - 1, 0) in zero_node_history:
        if (max_x, 1) in zero_node_history:
            break

# NEXT .... take all steps involving both zero-node and target-node to get target-node to (0,0)
