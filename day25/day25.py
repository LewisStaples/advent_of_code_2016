# adventOfCode 2016 day 25
# https://adventofcode.com/2016/day/25


import sys


TRY_NEXT_A = 100

list_input_instructions = []
list_output_clock_signal = []

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_string_list = in_string.split(' ')
        list_input_instructions.append(in_string_list)

# a = 0 # Need to find lowest positive integer that yields output a clock signal of 0, 1, 0, 1... repeating forever
a_init = 0
b = 0
c = 0
d = 0
instruction_number = 0


def cpy(in_str_list):
    if in_str_list[1].isnumeric():
        return
    value_to_be_copied = eval(in_str_list[0])
    globals()[in_str_list[1]] = value_to_be_copied


def inc(in_str_list):
    if in_str_list[0].isnumeric():
        return
    globals()[in_str_list[0]] += 1


def dec(in_str_list):
    if in_str_list[0].isnumeric():
        return
    globals()[in_str_list[0]] -= 1


def jnz_mult_shortcut(y, register_differences, in_str_list):
        for i in range(-1, y-1, -1):
            instruction = list_input_instructions[instruction_number + i]
            if instruction[0] == 'dec':
                register_differences[instruction[1]] -= 1
            elif instruction[0] == 'inc':
                register_differences[instruction[1]] += 1
            else:
                return False
        # Use multiplication jnz shortcut
        multiplier = -1 * globals()[in_str_list[0]] // register_differences[in_str_list[0]]
        for register, increment in register_differences.items():
            globals()[register] += increment * multiplier
        return True


def jnz(in_str_list):
    x = eval(in_str_list[0])
    y = eval(in_str_list[1])

    # Use multiplication jnz shortcut, if possible
    if in_str_list[0].isalpha():
        if not in_str_list[1].isalpha():
            register_differences = {'a':0, 'b':0, 'c':0, 'd':0}
            if y < 0:
                if jnz_mult_shortcut(y, register_differences, in_str_list):
                    return

    # The multiplication shortcut cannot be used, thus do manual jnz
    if x != 0:
        globals()['instruction_number'] += y - 1


def out(in_str_list):
    x = eval(in_str_list[0])
    list_output_clock_signal.append(x)

    if len(list_output_clock_signal) % 2 == x:
        return TRY_NEXT_A

    if len(list_output_clock_signal) > 10:
        print(list_output_clock_signal)
        print(f'The answer (the initial value of a which leads to an answer) is: {a_init}\n')
        sys.exit('Successful completion')

while True:
    a_init += 1
    a = a_init
    if a_init%100 == 0:
        print(a_init)

    while instruction_number < len(list_input_instructions):
        input_instruction = list_input_instructions[instruction_number]
        param_list_str = "(["
        for ele in input_instruction[1:]:
            param_list_str += '"'
            param_list_str += ele
            param_list_str += '"'
            param_list_str += ','
        param_list_str = param_list_str[0:-1]
        param_list_str += "])"
        ret_val = eval(input_instruction[0] + param_list_str)
        instruction_number += 1
        if ret_val == TRY_NEXT_A:
            list_output_clock_signal = []
            instruction_number = 0
            b = 0
            c = 0
            d = 0
            break



