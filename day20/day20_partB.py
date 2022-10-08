# adventOfCode 2016 day 20
# https://adventofcode.com/2016/day/20


from sympy import Interval, Union


all_invalid_numbers = dict()

input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        [lower, upper] = [int(x) for x in in_string.split('-')]
        all_invalid_numbers[lower] = upper

count_invalid_addresses = 0
upper_limit_valid_addresses = 4294967295 if len(all_invalid_numbers) > 10 else 9
current_union = Union(Interval(0,0))
for key in sorted(all_invalid_numbers.keys()):
    current_union = Union(current_union, Interval(key, all_invalid_numbers[key]))

    if len(current_union.boundary) == 4:
        four_points = list(current_union.boundary)
        four_points.sort()
        count_invalid_addresses += four_points[1] - four_points[0] + 1
        current_union = Union(Interval(four_points[2],four_points[3]))

count_invalid_addresses += current_union.args[1] - current_union.args[0] + 1

print(f'The count of permitted IPs is {upper_limit_valid_addresses + 1 - count_invalid_addresses}\n')

