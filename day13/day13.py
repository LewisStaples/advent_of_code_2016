# adventOfCode 2016 day 13
# https://adventofcode.com/2016/day/13


import sys

favorite_number = None
destination = None
inf = float('inf')

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()  
    favorite_number = int(in_string[34:])

    in_string = f.readline().rstrip()  
    destination = in_string[21:]
    destination = destination.split(',')
    destination = [int(x) for x in destination]
    destination = tuple(destination)

    in_string = f.readline().rstrip()
    number_of_steps = int(in_string[26:])

del in_string, input_filename, f

origin = (1,1)

print(f'Origin: {origin}')
print(f'Favorite number: {favorite_number}')
print(f'Intended destination: {destination}')
print(f'Number of steps (part B): {number_of_steps}')
print()

adjacent_directions = ((1,0), (-1,0),(0,1),(0,-1))

known_locations = {origin: 0}
locations_needing_neighbor_analysis = [origin]

while True:
    current_location = locations_needing_neighbor_analysis.pop(0)

    for adjacent_direction in adjacent_directions:
        # Define adjacent location
        adjacent_location = (current_location[0] + adjacent_direction[0], current_location[1] + adjacent_direction[1])
        # Check if valid
        if adjacent_location[0] < 0 or adjacent_location[1] < 0:
            continue
        # See if adjacent location has already been evaluated
        if adjacent_location in known_locations:
            # It's been evaluated already, so skip it
            continue
        
        # check if adjacent_location is a wall ... fill in with inf value and continue
        (x,y) = adjacent_location
        calc_value = x*x + 3*x + 2*x*y + y + y*y + favorite_number
        binary_string = bin(calc_value)
        if binary_string.count('1') % 2 == 1:
            # Adjacent location is a wall, therefore fill in with inf value and continue
            known_locations[adjacent_location] = inf
            continue

        # Since adjacent location is new and its not a wall, 
        # fill in its # of steps, and 
        known_locations[adjacent_location] = known_locations[current_location] + 1
        # Check if objective has been reached
        if adjacent_location == destination:
            print(f'The shortest path (answer to A) is {known_locations[adjacent_location]}\n')
            sys.exit('Program completed successfully\n')

        # plan to check out its adjacents
        locations_needing_neighbor_analysis.append(adjacent_location)

        if known_locations[adjacent_location] == number_of_steps:
            print(f'The number of locations reachable in {number_of_steps} steps (the last is the answer to B) is {len(known_locations) - len([x for x in known_locations.values() if x == inf])}\n')



