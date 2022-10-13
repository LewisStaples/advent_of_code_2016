# adventOfCode 2016 day 22
# https://adventofcode.com/2016/day/22


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        if line_num < 2:
            continue
        in_string = in_string.rstrip()
        print(in_string)
        in_fields = in_string.split()
        # print(in_string.split())
        print()




