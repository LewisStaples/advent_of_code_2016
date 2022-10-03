# adventOfCode 2016 day 17
# https://adventofcode.com/2016/day/17


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    passcode_str = f.readline().rstrip()
   
 
# Collection that lists all points on the board:
permissible_points = set()
for i in range(4):
    for j in range(4):
        permissible_points.add((i,j))
permissible_points.update([(3,4),(4,3),(4,4)])

current_paths = {():(0,0)}
next_paths = {}
while True:
    for path, point in current_paths.items():
        pass
        # for all possible directions (open doors)
            # compute hypothetical next point
            # if not in permissible_points, continue
            # add direction used to a deep copied path (no copying needed for the last one)
            # put new path and next point in dict next_paths
            # if next point is the destination, then we're finished
            #     the answer is the new path (convert to string of directions)

    break



