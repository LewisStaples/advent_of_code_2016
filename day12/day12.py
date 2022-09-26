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

def get_value(param):
    if isinstance(param, int):
        return param
    return eval(param)

a = 0
b = 0
c = 0  # manually change to 1 for part B
d = 0
instruction_number = 0

def cpy(in_str_list):
    value_to_be_copied = get_value(in_str_list[0])
    globals()[in_str_list[1]] = value_to_be_copied

def inc(in_str_list):
    globals()[in_str_list[0]] += 1

def dec(in_str_list):
    globals()[in_str_list[0]] -= 1

def jnz(in_str_list):
    x = get_value(in_str_list[0])
    y = get_value(in_str_list[1])
    if x != 0:
        globals()['instruction_number'] += y - 1

while instruction_number < len(list_input_instructions):
    input_instruction = list_input_instructions[instruction_number]
    param_list_str = "(["
    for ele in input_instruction[1:]:
        if ele.isdigit():
            param_list_str += ele
        else:
            param_list_str += '"'
            param_list_str += ele
            param_list_str += '"'
        param_list_str += ','
    param_list_str = param_list_str[0:-1]
    param_list_str += "])"
    eval(input_instruction[0] + param_list_str)

    instruction_number += 1

print(f'The answer (the final value of a) is: {a}')

