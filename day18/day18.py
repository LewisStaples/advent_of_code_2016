# adventOfCode 2016 day 18
# https://adventofcode.com/2016/day/18


def calc_num_rows(in_line):
    """Calculate number of rows to use for the line.

    This is based on the two input examples given, plus the graded problem to solve."""
    linelen_to_numrows = {5:3, 10:10, 100:40}
    return linelen_to_numrows[len(in_line)]

def get_new_row(old_row):
    """Determine what will be in the next row"""
    new_row = ''
    # Four alternative scenarios where a character in new_row will be a trap
    # Condition# 1: Its left and center tiles are traps, but its right tile is not.
    # Condition# 2: Its center and right tiles are traps, but its left tile is not.
    # Condition# 3: Only its left tile is a trap.
    # Condition# 4: Only its right tile is a trap.

    # for left-most character, the left is defined to be a safe tile, hence conditions 1 and 3 are impossible
    # The remaining conditions can be reduced to a single test
    if old_row[1] == '^':
        new_row += '^'
    else:
        new_row += '.'

    # for interior characters, all four conditions can be reduced to a single test
    for i in range(1, len(old_row) - 1):
        # print(f'index {i}: {old_row[i]}')
        if old_row[i-1] != old_row[i+1]:
            new_row += '^'
        else:
            new_row += '.'

    # for right-most character, the right is defined to be a safe tile, hence conditions 2 and 4 are impossible
    # The remaining conditions can be reduced to a single test
    if old_row[-2] == '^':
        new_row += '^'
    else:
        new_row += '.'

    return new_row


current_row = None

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file:  {input_filename}')
with open(input_filename) as f:
    first_row = f.readline().rstrip()
current_row = first_row
NUM_ROWS = calc_num_rows(current_row)
print(f'Contents of input file:  {current_row}')
print(f'Number of rows to calculate: {NUM_ROWS}\n')

safetile_count = 0
for i in range(NUM_ROWS):
    safetile_count += current_row.count('.')
    current_row = get_new_row(current_row)
print(f'The answer to part A is there are {safetile_count} safe tiles\n')

current_row = first_row
safetile_count = 0
for i in range(400000):
    safetile_count += current_row.count('.')
    current_row = get_new_row(current_row)
print(f'The answer to part B is there are {safetile_count} safe tiles\n')
