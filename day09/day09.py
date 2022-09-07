# adventOfCode 2016 day 09, part A
# https://adventofcode.com/2016/day/9


def decompress(in_string):
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

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(f'decomp_length: {len(decompress(in_string))}')
print()
