# adventOfCode 2016 day 09
# https://adventofcode.com/2016/day/9


def decompress_A(in_string):
    ret_val = ''
    i = 0
    while i < len(in_string):
        ch = in_string[i]
        if ch == '(':
            j = in_string.index(')', i)
            compr_params = [int(x) for x in in_string[i+1 : j].split('x')]
            for k in range(compr_params[1]):
                ret_val += in_string[j+1 : j+1+compr_params[0]]
            i = j+1+compr_params[0]
        else:
            ret_val += ch
            i += 1
    return ret_val

# Going to traverse the string from right to left and keeping count of added characters in a variable (an int).
# i is index of where the marker starts
# j is the index of where the marker ends
# m is the index of first index of string past that impacted by the marker
def len_decompress_B_recur(in_string):
    added_character_count = 0
    i = 0
    while i < len(in_string):
        ch = in_string[i]
        if ch == '(':
            j = in_string.index(')', i)
            compr_params = [int(x) for x in in_string[i+1 : j].split('x')]
            m = j + compr_params[0] + 1
            # count of chars. added = (characters added by marker's logic) - characters removed when the marker itself is removed
            added_character_count += (compr_params[0] * (compr_params[1] - 1)) - ( j - i + 1) + compr_params[1] * len_decompress_B_recur(in_string[j+1:m])
            i = m
        else:
            i += 1
    return added_character_count

def len_decompress_B(in_string):
    added_character_count = len_decompress_B_recur(in_string)
    return len(in_string) + added_character_count

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}:\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(f'{in_string}')
        if input_filename != 'input_sample1.txt':
            print(f'Part A decomp_length: {len(decompress_A(in_string))}')
        if input_filename != 'input_sample0.txt':
            print(f'Part B decomp_length: {len_decompress_B(in_string)}')
        print()
print()
