# adventOfCode 2016 day 13
# https://adventofcode.com/2016/day/13


import sys

favorite_number = None
destination = None
inf = float('inf')

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string1 = f.readline().rstrip()  
    favorite_number = int(in_string1[34:])

    in_string2 = f.readline().rstrip()  
    destination = in_string2[21:]
    destination = destination.split(',')
    destination = [int(x) for x in destination]
    destination = tuple(destination)


del in_string1, in_string2, input_filename, f

origin = (1,1)

print(f'Origin: {origin}')
print(f'Intended destination: {destination}')
print(f'Favorite number: {favorite_number}')
print()

adjacent_directions = ((1,0), (-1,0),(0,1),(0,-1))

known_locations = {origin: 0}
locations_needing_neighbor_analysis = [origin]

while True:
    current_location = locations_needing_neighbor_analysis.pop(0)

    for adjacent_direction in adjacent_directions:
        # Define adjacent location
        adjacent_location = (current_location[0] + adjacent_direction[0], current_location[1] + adjacent_direction[1])
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
            print(f'The shortest path (answer to A) is {known_locations[adjacent_location]}')
            sys.exit('Program completed successfully')

        # plan to check out its adjacents
        locations_needing_neighbor_analysis.append(adjacent_location)
