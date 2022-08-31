# adventOfCode 2016 day 02
# https://adventofcode.com/2016/day/2

import numpy as np


class Keypad:
    position_diff_matrix = {
        'D': np.array([+1,0]),
        'U': np.array([-1,0]),
        'R': np.array([0,+1]),
        'L': np.array([0,-1])
    }

    def __init__(self):
        self.layout = [
            ['' , '' , '' , '' , '' , '' , '' ],
            ['' , '' , '' , '1', '' , '' , '' ],
            ['' , '' , '2', '3', '4', '' , '' ],
            ['' , '5', '6', '7', '8', '9', '' ],
            ['' , '' , 'A', 'B', 'C', '' , '' ],
            ['' , '' , '' , 'D', '' , '' , '' ],
            ['' , '' , '' , '' , '' , '' , '' ]
        ]
        self.current_position = np.array([3,1])

    def get_current_value(self):
        x,y = self.current_position
        return self.layout[x][y]

    def update_current_position(self, move_char):
        new_position = self.current_position + Keypad.position_diff_matrix[move_char]
        if self.layout[new_position[0]][new_position[1]] == '':
            return
        self.current_position = new_position


my_keypad = Keypad()
bathroom_code = ''

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        for ch in in_string:
            my_keypad.update_current_position(ch)
        bathroom_code += my_keypad.get_current_value()

print(f'The answer to part B is: {bathroom_code}\n')



