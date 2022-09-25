# adventOfCode 2016 day 12
# https://adventofcode.com/2016/day/12


list_input_instructions = []

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_string_list = in_string.split(' ')
        list_input_instructions.append(in_string_list)

def cpy():
    pass

def inc():
    pass

def dec():
    pass

def jnz():
    pass

a = 0
b = 0
c = 0
d = 0

for input_instruction in list_input_instructions:
    print(input_instruction)
    eval(input_instruction[0])
