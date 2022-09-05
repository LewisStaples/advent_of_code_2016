# adventOfCode 2016 day 7
# https://adventofcode.com/2016/day/7


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

        # positions of left and right bracket characters
        i_left = [i for i,ch in enumerate(in_string) if ch == '[']
        i_right = [i for i,ch in enumerate(in_string) if ch == ']']

        # Test 1 ... len(i_left) should == len(i_right)
        assert(len(i_left) == len(i_right))
        # Test 2 ... i_left should be smallest, then an i_right should be next smallest, and so on
        for i in range(len(i_left)):
            assert(i_left[i] < i_right[i])
        for i in range(1, len(i_left)):
            assert(i_left[i] > i_right[i-1])
        # Above tests show that all brackets are in pairs with left followed by right bracket
        # without any nested brackets (this eliminates some nasty edge cases)
        
        i_all = i_left + i_right + [-1] + [len(in_string)] # combine i_left and i_right, plus start and end of the string
        i_all.sort()
        
        interior_strings = []
        exterior_strings = []

        for counter, i in enumerate(range(1, len(i_all))):
            new_string = in_string[i_all[i-1] + 1: i_all[i]]
            if counter%2 == 0:
                exterior_strings.append(new_string)
            else:
                interior_strings.append(new_string)
        dummy = 123
        print(f'interior: {interior_strings}, exterior: {exterior_strings}\n')

