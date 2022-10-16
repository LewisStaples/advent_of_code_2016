# adventOfCode 2016 day 22
# https://adventofcode.com/2016/day/22

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

node_list = []
count_valid_pairs = 0
Node = namedtuple('Node', ['Filesystem', 'Size', 'Used', 'Avail', 'UsePct'])
target_x = 0

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
        target_x = max(target_x, get_x_coordinate(in_fields[0]))
        node_list.append(Node(*in_fields))

largest_size = 0
smallest_size = float('inf')
largest_used = 0
smallest_used = float('inf')

large_nodes = set()
for i, nodeA in enumerate(node_list):
    if nodeA.Used > 100:
        large_nodes.add(nodeA)
        continue
    if nodeA.Used == 0:
        print('Used is zero at node: ', end='')
        print(nodeA)
        print(f'This is at coordinates:({get_x_coordinate(nodeA.Filesystem)},{get_y_coordinate(nodeA.Filesystem)})')

    else:
        smallest_used = min(smallest_used, nodeA.Used)
        largest_size = max(largest_size, nodeA.Size)

    smallest_size = min(smallest_size, nodeA.Size)
    largest_used = max(largest_used, nodeA.Used)


print()
for large_node in large_nodes:
    print('Large usage node is: ', end='')
    print(large_node, end='')
    print(f', at coordinates: ({get_x_coordinate(nodeA.Filesystem)},{get_y_coordinate(nodeA.Filesystem)})')
    
print(f'\nLargest size found in any node (except for those listed as large above): {largest_size}')
print(f'Smallest size found in any node: {smallest_size}')
print(f'Largest used found in any node (except for those listed as large above): {largest_used}')
print(f'Smallest used found in any node (except for the zero used node above): {smallest_used}\n')

print(f'The "target" node is at coordinates: ({target_x}, 0)\n')
