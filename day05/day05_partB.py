# adventOfCode 2016 day 5
# https://adventofcode.com/2016/day/5

import hashlib

PASSWORD_LENGTH = 8
ZERO_PAD_NUMBER = 5

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()

integer_index = 0
number_matches_found = 0
password_list_B = [None] * PASSWORD_LENGTH

while True:
    hash_input_str = in_string + str(integer_index)
    hash_output_str = hashlib.md5(hash_input_str.encode()).hexdigest()
    integer_index += 1
    if hash_output_str[:ZERO_PAD_NUMBER] == '0'*ZERO_PAD_NUMBER:
        password_index = hash_output_str[5]
        if not password_index.isdigit():
            # "ignore invalid positions" (non-number is invalid)
            continue
        password_index = int(password_index)
        if password_index not in range(PASSWORD_LENGTH):
            # "ignore invalid positions" (number is outside of range)
            continue
        if password_list_B[password_index] != None:
            # "Use only the first result for each position"
            continue
        number_matches_found += 1
        password_list_B[password_index] = hash_output_str[6]
        if number_matches_found == PASSWORD_LENGTH:
            break

print('The password (solution for part B) is ', end = '')
print(''.join(password_list_B))
print()



