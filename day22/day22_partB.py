# adventOfCode 2016 day 22
# https://adventofcode.com/2016/day/22


from collections import namedtuple
import sys


node_used_tuple = []
NODE_AVAIL_DICT = dict()
UsedNode = namedtuple('Node', ['GridCoords', 'Used'])
max_x = 0

def modify_input_field(in_string):
    # Remove T units at end of memory values
    if not in_string.isdigit():
        if in_string[:-1].isdigit():
            return int(in_string[:-1])
    # Convert filesystem field into grid coordinates
    grid_coords = in_string[16:].split('-y')
    grid_coords = [int(x) for x in grid_coords]
    return tuple(grid_coords)


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        if line_num < 2:
            continue
        in_string = in_string.rstrip()
        in_fields = in_string.split()
        in_fields = [modify_input_field(x) for x in in_fields]
        in_fields_used = [in_fields[0], in_fields[2]]
        node_used_tuple.append(UsedNode(*in_fields_used))
        NODE_AVAIL_DICT[in_fields[0]] = in_fields[3]
        max_x = max(max_x, in_fields[0][0])
node_used_tuple.insert(0, (max_x,0))
node_dicts = dict()
node_dicts[tuple(node_used_tuple)] = 0
moves_complete = 0

while True:
    node_used_tuple_list = []
    for node_used_tuple, i in node_dicts.items():
        if i == moves_complete:
            node_used_tuple_list.append(node_used_tuple)

    for node_used_tuple in node_used_tuple_list:
        for i, nodeA in enumerate(node_used_tuple[1:]):
            # Eliminate pairs where nothing gets moved
            if nodeA.Used == 0:
                continue
            for j, nodeB in enumerate(node_used_tuple[1:]):
                # Eliminate "pairs" with the same node is repeated
                if i == j:
                    continue
                # Eliminate pairs that aren't adjacent
                if abs(nodeA.GridCoords[0] - nodeB.GridCoords[0]) + abs(nodeA.GridCoords[1] - nodeB.GridCoords[1]) >= 2:
                    continue
                # Elminate pairs where nodeA is the target and nodeB has more than zero memory
                if nodeA.GridCoords == node_used_tuple[0]:
                    if nodeB.Used > 0:
                        continue
                # Eliminate pairs where there is not enough available space to move to
                if nodeA.Used <= NODE_AVAIL_DICT[nodeB.GridCoords]:
                    # do something with them
                    node_used_tuple__new = [] # starting with a list
                    for node in node_used_tuple:
                        if node == nodeA:
                            node_used_tuple__new.append(nodeB)
                        elif node == nodeB:
                            node_used_tuple__new.append(nodeA)
                            # If moved node is the target
                            if nodeA.GridCoords == node_used_tuple[0]:
                                pass
                                # Update targets' location
                                node_used_tuple__new[0] = nodeB.GridCoords
                                if node_used_tuple__new[0] == (0,0):
                                    sys.exit('The problem is now solved')
                                # If target has reached (0,0), the problem is now solved

                        else:
                            node_used_tuple__new.append(node)
                    node_used_tuple__new = tuple(node_used_tuple__new)
 
                    dummy = 123

                    if node_used_tuple__new not in node_dicts:
                        node_dicts[node_used_tuple__new] = moves_complete + 1
    # break
    moves_complete += 1



