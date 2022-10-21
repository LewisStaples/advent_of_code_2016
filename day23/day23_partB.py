# adventOfCode 2016 day 23
# https://adventofcode.com/2016/day/23



list_input_instructions = []

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_string_list = in_string.split(' ')
        list_input_instructions.append(in_string_list)

a = 0 if input_filename == 'input_sample0.txt' else 12
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
        # Use multiplication jnz shortcut (it's been shown to be possible)
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

def tgl(in_str_list):
    index_tgl_instruction = eval(in_str_list[0]) + globals()['instruction_number']
    # "If an attempt is made to toggle an instruction outside the program, nothing happens."
    if True in [index_tgl_instruction < 0, index_tgl_instruction >= len(globals()['list_input_instructions'])]:
        return

    toggle_command = {
        'inc':'dec',
        'dec':'inc',
        'jnz':'cpy',
        'cpy':'jnz',
        'tgl':'inc'
    }
    globals()['list_input_instructions'][index_tgl_instruction][0] = toggle_command[globals()['list_input_instructions'][index_tgl_instruction][0]]

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
    eval(input_instruction[0] + param_list_str)
    instruction_number += 1

print(f'The answer (the final value of a) is: {a}\n')

