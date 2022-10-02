# adventOfCode 2016 day 16
# https://adventofcode.com/2016/day/16


# Reading input from the input file
input_filename='input_B.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    current_state = list(f.readline().rstrip()[14:])
    current_state = [int(x) for x in current_state]
    disk_length = int(f.readline().rstrip()[12:])
   
# Parsing input file   
print('Initial values:')
print(current_state)
print(disk_length)
print()

bin_not_dict = {0:1, 1:0}
while len(current_state) < disk_length:
    reversed_chars = current_state[::-1]
    reversed_chars = [bin_not_dict[x] for x in reversed_chars]
    current_state.append(0)
    current_state.extend(reversed_chars)

# truncate unneeded chars
current_state = current_state[:disk_length]

# work on the checksum
while len(current_state)%2 == 0:
    len_cur_st = len(current_state)
    for i in range(len_cur_st - 2, -1, -2):
        current_state[i] = (current_state[i] + current_state[i + 1] + 1) % 2
        del current_state[i + 1]

print(f'The answer is {"".join([str(x) for x in current_state])}\n')



