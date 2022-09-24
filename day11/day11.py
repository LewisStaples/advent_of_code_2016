# adventOfCode 2016 day 11
# https://adventofcode.com/2016/day/11

# import copy
# import itertools
import sys


# List of lists showing the current state
current_state = [[], [], 1, 0]

def invalid_state(state):
    for i, chip_index in enumerate(state[0]):
        gen_index = state[1][chip_index]
        # If chip and generator are both on the same floor
        if chip_index == gen_index:
            # this particular chip is safe
            continue
        # Since this chip's generator is on another floor,
        # if there are any generators on this floor
        if chip_index in state[1]:
            # This chip would get damaged by the generator, so the state is invalid
            return True

    # No chips have generators that are a threat, thus the state is valid (hence, not invalid)
    return False

# This converts to tuples to lists.
def make_state_mutable(state_immutable, ele_floor, step_count):
    mutable_state = [list(state_immutable[0]), list(state_immutable[1]), ele_floor, step_count]
    # for 
    return mutable_state



# This converts lists to tuples.  It also orders chips in ascending order and re-orders the generators to continue to match the chips
def make_state_immutable(state):
    new_state_0 = sorted(state[0])
    new_state_1 = [x for _,x in sorted(zip(state[0],state[1]))]
    return_state = (tuple(new_state_0), tuple(new_state_1))
    return return_state, state[2], state[3]

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    floor_num_lookup = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
    
    # Used to store data coming from the text file, before re-processing it later
    initial_state_gens = dict()
    initial_state_chips = dict()
    
    for i in range(1,5):
        initial_state_chips[i] = []

    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

        # Remove "The "
        assert(in_string[0:4] == 'The ')
        in_string = in_string[4:]


        # Get floor number from input file
        floor_num_str, floor_dummy, contains_dummy, in_string = in_string.split(' ', 3)
        floor_num = floor_num_lookup[floor_num_str]
        del floor_dummy, contains_dummy, floor_num_str

        # Loop through all devices on this line in input file (they're all on the same floor)
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

del floor_num_lookup

for floor_chip in range(1, 5):
    for element in initial_state_chips[floor_chip]:
        floor_gen = initial_state_gens[element]
        current_state[0].append(floor_chip)
        current_state[1].append(floor_gen)


current_state_immutable, ele_floor, step_count = make_state_immutable(current_state)
known_states = {current_state_immutable: (ele_floor, step_count)}


while True:
    # current_state = next_states.pop(0):
    current_state_immutable, ele_floor, step_count = make_state_immutable(current_state)
    if current_state_immutable not in known_states:
        # check if this is the answer ... if yes ... output the solution
        if set(current_state[0]) == {4} and set(current_state[1]) == {4}:
            print(f'The answer to A has been found:  {step_count} steps are required')
            sys.exit('Program exiting successfully')
        known_states[current_state_immutable] = (ele_floor, step_count)

        current_state = make_state_mutable(current_state_immutable, ele_floor, step_count)
        # determine adjacent states, and add valid states to next_states
    break

print('Program has ended without finding the answer\n')

# current_states_list.append(current_state)
# current_states_set.add(convert_state_to_hashable(current_state))





