# adventOfCode 2016 day 21
# https://adventofcode.com/2016/day/21


test = False

def swap(param_list, password):
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

def do_right_rotation(number_right_steps, password):
    for i in range(number_right_steps):
        letter = password.pop()
        password.insert(0, letter)
    return password

def rotate(param_list, password):
    if len(param_list) == 3:
        number_steps = int(param_list[1])
        if param_list[0] == 'right':
            do_right_rotation(number_steps, password)
        elif param_list[0] == 'left':
            do_right_rotation(len(password) - number_steps, password)
        else:
            raise ValueError('Bad parameter')
    elif len(param_list) == 6:
        assert param_list[:5] == ['based', 'on', 'position', 'of', 'letter']
        letter = param_list[5]
        index = password.index(letter) + 1
        if index >= 5:
            index += 1
        do_right_rotation(index, password)
    return password

def reverse(param_list, password):
    assert param_list[0] == 'positions'
    assert param_list[2] == 'through'
    i1, i2 = int(param_list[1]), int(param_list[3])
    ret_val = password[:i1]
    for ele in reversed(password[i1:i2+1]):
        ret_val.append(ele)
    for ele in password[i2+1:]:
        ret_val.append(ele)
    return ret_val

def move(param_list, password):
    assert param_list[0] == 'position'
    assert param_list[2] == 'to'
    assert param_list[3] == 'position'
    i1, i2 = int(param_list[1]), int(param_list[4])
    the_letter = password.pop(i1)
    password.insert(i2, the_letter)
    return password

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
password = 'abcde' if input_filename=='input_sample0.txt' else 'abcdefgh'
password = list(password)
print('Initial password: ' + ''.join(password) + '\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if test:
            print(f'After processing command ... {in_string}')
        in_string = in_string.split(' ')
        password = locals()[in_string[0]](in_string[1:], password)
        if test:
            print('password = ' + ''.join(password) + '\n')

print('The answer to part A is: ' + ''.join(password) + '\n')