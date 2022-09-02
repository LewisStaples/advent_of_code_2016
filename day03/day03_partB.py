# adventOfCode 2016 day 03, part B
# https://adventofcode.com/2016/day/03


possible_triangle_count = 0
triangle_sides = [[], [], []]
# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()

        sides_line = [int(x) for x in [in_string[2:5], in_string[7:10], in_string[12:15]]]
        for i, side in enumerate(sides_line):
            triangle_sides[i].append(side)
        
        if len(triangle_sides[0]) == 3:
            for i in range(len(triangle_sides)):
                triangle_sides[i].sort()
                if triangle_sides[i][0] + triangle_sides[i][1] > triangle_sides[i][2]:
                    possible_triangle_count += 1
                triangle_sides[i].clear()

print(f'The answer to part B is {possible_triangle_count}')

