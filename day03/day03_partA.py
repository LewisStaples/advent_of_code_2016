# adventOfCode 2016 day 03, part A
# https://adventofcode.com/2016/day/03


possible_triangle_count = 0

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        triangle_sides = [int(x) for x in [in_string[2:5], in_string[7:10], in_string[12:15]]]
        triangle_sides.sort()
        if triangle_sides[0] + triangle_sides[1] > triangle_sides[2]:
            possible_triangle_count += 1

print(f'The answer to part A is {possible_triangle_count}')

