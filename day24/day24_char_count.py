# adventOfCode 2016 day 24
# https://adventofcode.com/2016/day/24


from collections import Counter

char_count = dict()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        the_counter = Counter(in_string)
        for ch, count in the_counter.items():
            if ch in char_count:
                char_count[ch] += count
            else:
                char_count[ch] = count
    print()
    for ch, count in char_count.items():
        print(f'{ch} appears {count} time(s)')
    print()

