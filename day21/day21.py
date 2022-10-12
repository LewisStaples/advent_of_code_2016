# adventOfCode 2016 day 21
# https://adventofcode.com/2016/day/21


import copy

# Setting test to True shows all commands from input and each command's resulting intermediate password for both parts A and B
# For part B, setting test to True also shows the trials used in the trial and error associated with "rotate based on position of letter X"
# For part B, setting test to True uses part A password backwards (which is wrong for the graded problem), but this can be used to observe that the backwards process is the same as the forwards process.

test = False
# test = True

def swap(param_list, password, reverse = False):
    assert param_list[2] == 'with'
    indices_to_swap = list()
    for i in [0,3]:
        assert param_list[i] in ('position', 'letter')
        if param_list[i] == 'position':
            assert param_list[i+1].isdigit()
            indices_to_swap.append(int(param_list[i+1]))
        elif param_list[i] == 'letter':
            indices_to_swap.append(password.index(param_list[i+1]))
    ch0, ch1 = password[indices_to_swap[0]], password[indices_to_swap[1]]
    password[indices_to_swap[0]] = ch1
    password[indices_to_swap[1]] = ch0
    return password

def do_right_rotation(number_right_steps, password, reverse = False):
    for i in range(number_right_steps):
        if reverse:
            letter = password.pop(0)
            password.append(letter)
        else:
            letter = password.pop()
            password.insert(0, letter)
    return password

def rotate(param_list, password, reverse = False):
    if len(param_list) == 3:
        number_steps = int(param_list[1])
        if param_list[0] == 'right':
            do_right_rotation(number_steps, password, reverse)
        elif param_list[0] == 'left':
            do_right_rotation(len(password) - number_steps, password, reverse)
        else:
            raise ValueError('Bad parameter')
    elif len(param_list) == 6:
        if reverse == False:
            assert param_list[:5] == ['based', 'on', 'position', 'of', 'letter']
            letter = param_list[5]
            index = password.index(letter) + 1
            if index >= 5:
                index += 1
            do_right_rotation(index, password, False)
        else:  # if reverse is True
            # Trial and error
            good_i_set = set()
            for i in range(len(password)):
                password_trial = copy.deepcopy(password)
                password_trial = do_right_rotation(i, password_trial, False)
                password_trial = rotate(param_list, password_trial, False)
                if test:
                    print(f'Trial {i}: {password}, {password_trial}, {password == password_trial}')
                if password == password_trial:
                    good_i_set.add(i)
            assert len(good_i_set) == 1
            password = do_right_rotation(good_i_set.pop(), password, False)
    return password

def reverse(param_list, password, reverse = False):
    assert param_list[0] == 'positions'
    assert param_list[2] == 'through'
    i1, i2 = int(param_list[1]), int(param_list[3])
    ret_val = password[:i1]
    for ele in reversed(password[i1:i2+1]):
        ret_val.append(ele)
    for ele in password[i2+1:]:
        ret_val.append(ele)
    return ret_val

def move(param_list, password, reverse = False):
    assert param_list[0] == 'position'
    assert param_list[2] == 'to'
    assert param_list[3] == 'position'
    i1, i2 = int(param_list[1]), int(param_list[4])
    if reverse:
        i1, i2 = i2, i1
    the_letter = password.pop(i1)
    password.insert(i2, the_letter)
    return password

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')

# Part A problem
password = 'abcde' if input_filename=='input_sample0.txt' else 'abcdefgh'
password = list(password)
print('Part A initial password: ' + ''.join(password))
if test:
    print()
with open(input_filename) as f:
    # Pull in each line from the input file
    file_input = list()
    for in_string in f:
        in_string = in_string.rstrip()
        if test:
            print(f'After processing command ... {in_string}')
        in_string = in_string.split(' ')
        password = locals()[in_string[0]](in_string[1:], password)
        if test:
            print('password = ' + ''.join(password) + '\n')
        file_input.append(in_string)
print('The answer to part A is: ' + ''.join(password) + '\n')


# Part B problem

# This attempts to reverse the sample from part A:
if input_filename=='input_sample0.txt':
    password = 'decab'

# This solves the given problem to solve:
if not test and input_filename=='input.txt':
    password = 'fbgdceah'

# Otherwise (if test and using input.txt, it will succesfully reverse the original problem):
password = list(password)
print('Part B initial password: ' + ''.join(password))
if test:
    print()
for i in range(len(file_input)-1, -1, -1):
    in_string = file_input[i]
    if test:
        print(f'After processing command (in list format) ... {in_string}')
    password = locals()[in_string[0]](in_string[1:], password, reverse = True)
    if test:
        print('password = ' + ''.join(password) + '\n')

print('The answer to part B is: ' + ''.join(password) + '\n')
