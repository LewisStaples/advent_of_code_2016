# adventOfCode 2016 day 6
# https://adventofcode.com/2016/day/6

import itertools

class Keypad:
    def __init__(self, width, length):
        self.pixel_set = set()
        self.WIDTH = width
        self.LENGTH = length
        
    def rect(self, x, y):
        the_points = itertools.product(list(range(x)), list(range(y)))
        for point in the_points:
            self.pixel_set.add((point[0],point[1]))
        
    def display(self):
        print()
        for b in range(self.LENGTH):
            for a in range(self.WIDTH):
                if (a,b) in self.pixel_set:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()

    def rotate(self, axis, axis_value, shift_number):
        new_pixel_set = set()
        for old_point in self.pixel_set:
            if old_point[axis] == axis_value:
                new_point = (
                    (old_point[0] + shift_number) % self.WIDTH if axis == 1 else old_point[0] ,
                    (old_point[1] + shift_number) % self.LENGTH if axis == 0 else old_point[1]
                )
                new_pixel_set.add(new_point)
            else:
                new_pixel_set.add(old_point)
        self.pixel_set = new_pixel_set

    def get_num_pixels(self):
        return len(self.pixel_set)

the_keypad = None
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for i, in_string in enumerate(f):
        in_string = in_string.rstrip()
        if i == 0:
            # This supports the sample example given 
            # and the below 50,6 supports the gradable problem
            # (since my gradable input has a different first line)
            if in_string == 'rect 3x2':
                the_keypad = Keypad(7, 3)
            else:
                the_keypad = Keypad(50, 6)
        in_string = in_string.rstrip()
        command, parameters = in_string.split(' ', 1)

        if command == 'rect':
            parameters_parsed = [int(x) for x in parameters.split('x')]
            the_keypad.rect(parameters_parsed[0], parameters_parsed[1])
        elif command == 'rotate':
            axis_variable_composite, shift_var = parameters.split(' by ')
            axis_var_string, axis_value_var = axis_variable_composite.split('=')
            axis_value_var = int(axis_value_var)
            shift_var = int(shift_var)
            axis_var = 0 if axis_var_string == 'column x' else 1
            the_keypad.rotate(axis_var, axis_value_var, shift_var)
        the_keypad.display()

print(f'The answer to part A is {the_keypad.get_num_pixels()}\n')

