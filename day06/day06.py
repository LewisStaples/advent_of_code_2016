# adventOfCode 2016 day 6
# https://adventofcode.com/2016/day/6

import collections

class LetterFreq:
    def __init__(self, in_string):
        self.column_list = []
        for ch in in_string:
            self.column_list.append([ch])

    def add(self, in_string):
        for i,ch in enumerate(in_string):
            self.column_list[i].append(ch)

    def decrypt(self):
        ret_val_A = ''
        ret_val_B = ''
        for col_list in self.column_list:
            ret_val_A += collections.Counter(col_list).most_common(1)[0][0]
            ret_val_B += collections.Counter(col_list).most_common(None)[-1][0]
        return ret_val_A, ret_val_B

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        in_string = in_string.rstrip()
        if 0 == line_num:
            letter_freq = LetterFreq(in_string)
        else:
            letter_freq.add(in_string)

solutions = letter_freq.decrypt()
print(f'The solution to part A is: {solutions[0]}')
print(f'The solution to part A is: {solutions[1]}\n')
