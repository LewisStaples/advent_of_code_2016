# adventOfCode 2016 day 5
# https://adventofcode.com/2016/day/5

import hashlib


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()

integer_index = 0
number_matches_found = 0
password_str_A = ''

while True:
    hash_input_str = in_string + str(integer_index)
    hash_output_str = hashlib.md5(hash_input_str.encode()).hexdigest()

    if hash_output_str[:5] == '00000':
        number_matches_found += 1
        password_str_A += hash_output_str[5]
    integer_index += 1
    if number_matches_found == 8:
        break

print(f'The password (solution for part A) is {password_str_A}\n')

