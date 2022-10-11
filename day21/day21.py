# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??


def swap(param_list):
    pass

def reverse(param_list):
    pass

def rotate(param_list):
    pass

def move(param_list):
    pass

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
password = 'abcde' if input_filename=='input_sample0.txt' else 'abcdefgh'
password = list(password)
print('Initial password: ' + ''.join(password) + '\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip().split(' ')

        locals()[in_string[0]](in_string[1:])
        # output
        print(f'After processing command ... {in_string}')
        print('password = ' + ''.join(password) + '\n')


