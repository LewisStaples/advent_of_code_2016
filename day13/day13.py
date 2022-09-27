# adventOfCode 2016 day 13
# https://adventofcode.com/2016/day/13


favorite_number = None
destination = None

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string1 = f.readline().rstrip()  
    favorite_number = int(in_string1[34:])

    in_string2 = f.readline().rstrip()  
    destination = in_string2[21:]
    destination = destination.split(',')
    destination = [int(x) for x in destination]
    destination = tuple(destination)


