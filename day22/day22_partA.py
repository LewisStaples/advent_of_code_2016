# adventOfCode 2016 day 22
# https://adventofcode.com/2016/day/22


from collections import namedtuple

node_list = []
count_valid_pairs = 0
Node = namedtuple('Node', ['Filesystem', 'Size', 'Used', 'Avail', 'UsePct'])

def remove_unit(in_string):
    if not in_string.isdigit():
        if in_string[:-1].isdigit():
            return int(in_string[:-1])
    return in_string

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
        node_list.append(Node(*in_fields))

for i, nodeA in enumerate(node_list):
    if nodeA.Used == 0:
        continue
    for j, nodeB in enumerate(node_list):
        if i == j:
            continue
        if nodeA.Used <= nodeB.Avail:
            count_valid_pairs += 1

print(f'The answer to part A is {count_valid_pairs}\n')


