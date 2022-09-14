# adventOfCode 2016 day 11
# https://adventofcode.com/2016/day/11

import csv
import copy
import itertools

# Using below data as periodic_table.csv
# https://gist.github.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee
with open('periodic_table.csv', mode='r') as element_file:
    reader = csv.reader(element_file)
    element_to_abbrev = {(rows[1].lower()):rows[2] for rows in reader if rows[1] != 'Element'}

previous_states_set = set()
current_states_list = list()
current_states_set = set()
future_states_list = list()
future_states_set = set()

# Dict showing the current state
current_state = dict()

def invalid_combination(combination):
    generator_types = set()
    microchip_types = set()
    for component in combination:
        if component[-1] == 'G':
            # generator_types.
            generator_types.add(component[:-2])
        elif component[-1] == 'M':
            microchip_types.add(component[:-2])
    
    # If there are any microchips
    if len(generator_types) > 0:
        # and if there are any generators without a matching microchip
        if len(microchip_types - generator_types) > 0:
            return False
    
    return True

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    floor_num_lookup = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

        # Remove "The "
        assert(in_string[0:4] == 'The ')
        in_string = in_string[4:]

        # Get floor number
        floor_num_str, floor_dummy, contains_dummy, in_string = in_string.split(' ', 3)
        floor_num = floor_num_lookup[floor_num_str]
        del floor_dummy, contains_dummy, floor_num_str

        while True:
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
            index_str = element_to_abbrev[in_string[2:i_right]] + '-' + ('M' if in_string[i_right] == '-' else 'G')
            in_string = in_string[in_string.find('a ', 1):]
            current_state[index_str] = floor_num
current_state['Elev.'] = 1
# del floor_num_lookup

current_states_list.append(current_state)
current_states_set.add(tuple(sorted(current_state.items())))

while True:
    # Traverse current_states_list
    for current_state in current_states_list:
        current_floor = current_state['Elev.']
        current_floor_items = {item for item in current_state if current_state[item] == current_floor and item != 'Elev.'}

        # Consider new floors for elevator
        for floor_delta in [-1,1]:
            new_floor = current_floor + floor_delta
            if new_floor in floor_num_lookup.values():
                new_state = copy.deepcopy(current_state)
                new_state['Elev.'] += floor_delta
                future_states_list.append(new_state)
        
        # look for anything else on current state's floor that could be brought to new_state's floor
        choices_to_move = list(itertools.combinations(current_floor_items, 1)) + list(itertools.combinations(current_floor_items, 2))
        for choice_move in choices_to_move:
            # Determine what choice_move will leave behind
            left_behind = current_floor_items - set(choice_move)
            if invalid_combination(left_behind):
                continue
            for new_state in future_states_list:
                new_floor = new_state['Elev.']
                newest_state = copy.deepcopy(new_state)
                for item_to_move in choice_move:
                    newest_state[item_to_move] = new_floor
                    if invalid_combination([item for item, floor in newest_state.items() if floor == new_floor]):
                        continue
                    # future_states_list.append(newest_state)
                    newest_state_tuple = tuple(sorted(newest_state.items()))
                    if newest_state_tuple not in previous_states_set and newest_state_tuple not in current_states_set:
                        future_states_set.add(newest_state_tuple)
    
    previous_states_set.update(current_states_set)
    current_states_set.clear()
    current_states_set.update(future_states_set)
    future_states_set.clear()
    current_states_list.clear()

    for current_state_tuple in current_states_set:
        current_state_dict = dict()
        for key, value in current_state_tuple:
            current_state_dict[key] = value
        
        if set(current_state_dict.values()) == {4}:
            break

        current_states_list.append(current_state_dict)
    future_states_list = list()



        # For each current_state, come up with future_states
            # degrees of freedom:
            # Elevator can only go up or down by one floor
            # Elevator must carry either 1 or 2 items
            # constraints
            # Elevator cannot go outside of floors [1,4]
            # You can't have a generator along with a non-matching chip on any floor, including elevator

        # Verify that that future state isn't already in any set




