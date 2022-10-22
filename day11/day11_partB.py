# adventOfCode 2016 day 11
# https://adventofcode.com/2016/day/11


import itertools
import sys


# Detect if this state is not valid
def invalid_state(state):
    for chip_index, chip_floor in enumerate(state[0]):
        gen_floor = state[1][chip_index]
        # If chip and generator are both on the same floor
        if chip_floor == gen_floor:
            # this particular chip is safe
            continue
        # Since this chip's generator is on another floor,
        # If there are any generators on this chip's floor
        if chip_floor in state[1]:
            # This chip will get damaged by the generator, so the state is invalid
            return True

    # No chips have generators that are a threat, thus the state is valid (hence, not invalid)
    return False

# This orders chips in ascending order and re-orders the generators to continue to match the chips
def sort_state(state):
    new_state_0 = sorted(state[0])
    new_state_1 = [x for _,x in sorted(zip(state[0],state[1]))]
    return tuple(new_state_0), tuple(new_state_1), state[2]


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename} (Input file contents are shown below)\n')
with open(input_filename) as f:
    floor_num_lookup = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
    
    # Used to store data coming from the text file, before re-processing it later
    initial_state_gens = dict()
    initial_state_chips = dict()
    
    for i in range(1,5):
        initial_state_chips[i] = []
    del i

    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

        # Remove "The "
        assert(in_string[0:4] == 'The ')
        in_string = in_string[4:]

        # Get floor number from input line
        floor_num_str, floor_dummy, contains_dummy, in_string = in_string.split(' ', 3)
        floor_num = floor_num_lookup[floor_num_str]
        del floor_dummy, contains_dummy, floor_num_str

        # Loop through all devices on this line (they're all on the same floor)
        # Fill in initial_state_gens and initial_state_chips
        while True:
            # Find the index of the next device
            i_chip = in_string.find('-compatible microchip')
            i_gen = in_string.find(' generator')
            if i_chip == i_gen == -1:
                # both find commands returned -1, thus neither string was found
                break
            if i_chip == -1:
                i_right = i_gen
            elif i_gen == -1:
                i_right = i_chip
            else:
                i_right = min(i_gen, i_chip)
            
            index_str = in_string[2:i_right]
            if in_string[i_right] == '-':
                initial_state_chips[floor_num].append(index_str)
            else:
                initial_state_gens[index_str] = floor_num
            in_string = in_string[in_string.find('a ', 1):]
print()

del floor_num_lookup, i_chip, i_gen, i_right, floor_num, index_str
del input_filename, f, in_string
# Defining indices in current_state_L (note the _L indicates it has lists ... without the L has tuples)
# index 0:  ordered list of floor numbers with a chip
# index 1:  list of floor numbers with a generator
# (each generator is at the same index as its matching chip)
# index 2:  elevator floor
current_state_L = [[], [], 1]
for floor_chip in range(1, 5):
    for element in initial_state_chips[floor_chip]:
        floor_gen = initial_state_gens[element]
        current_state_L[0].append(floor_chip)
        current_state_L[1].append(floor_gen)
del floor_chip, floor_gen, element, initial_state_chips, initial_state_gens

print('Since this is a part B problem, two pairs of matching chips and generators are added to the first floor')
print('The instructions call them elerium and dilithium, but the names do not impact the resulting count\n')
current_state_L[0].insert(0,1)
current_state_L[0].insert(0,1)
current_state_L[1].insert(0,1)
current_state_L[1].insert(0,1)

# Convert from using lists to using tuples
current_state = tuple(
    [
        tuple(current_state_L[0]),
        tuple(current_state_L[1]),
        current_state_L[2]
    ]
)
del current_state_L

known_states = dict()
current_time = 0
known_states[current_state] = current_time
next_elevator_floor_map = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}

while True:
    states_to_check = [k for k, v in known_states.items() if v == current_time]
    current_time += 1
    for current_state in states_to_check:
        # Identify elevator's current floor
        this_ele_fl = current_state[2]
        # List all devices on the same floor as the elevator
        devices_on_this_fl = set()
        for chip_index, value in enumerate(current_state[0]):
            if value == this_ele_fl:
                devices_on_this_fl.add((0,chip_index))
        del chip_index, value

        for index, value in enumerate(current_state[1]):
            if value == this_ele_fl:
                devices_on_this_fl.add((1,index))
        del index, value
        # Looping through all valid next elevator floors
        for next_ele_fl in next_elevator_floor_map[current_state[2]]: 
            # Use itertools to consider all possible single devices, plus all pairs of devices
            device_move_options = list(itertools.permutations(devices_on_this_fl, 2))
            device_move_options += list(itertools.permutations(devices_on_this_fl, 1))
            for move in device_move_options:
                # Construct potential new state
                new_state = [
                    list([x for x in current_state[0]]),
                    list([x for x in current_state[1]]),
                    next_ele_fl
                ]
                for move_piece in move:
                    new_state[move_piece[0]][move_piece[1]] = next_ele_fl
                
                # re-sort and convert to tuple
                new_state = sort_state(new_state)

                # Verify that new state isn't already in known_states
                if new_state in known_states:
                    continue
                # Check if it is invalid
                if invalid_state(new_state):
                    continue
                # Check if it has solved the problem
                # check if this is the answer ... if yes ... output the solution
                if set(new_state[0]) == {4} and set(new_state[1]) == {4}:
                    print(f'The answer to B has been found:  {current_time} steps are required\n')
                    sys.exit('Program exiting successfully')

                known_states[new_state] = current_time

