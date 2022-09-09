# Thinking through approach

# Verify that all bots listed in commands as receiving chips have a line showing what they do with received bots

# Get set of all bots in lines starting with "bot" with the bot_number immediately after that
# This is the set of commands showing what to do with the bots

# Find bot anywhere else in any line, and create another set of bot_number values immediately after that

# See if both sets of bot numbers are identical

set_bots_start = set()
set_bots_later = set()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_string = in_string.split(' ')

        if in_string[0] == 'bot':
            set_bots_start.add(int(in_string[1]))
        for i in range(2, len(in_string)-1):
            if in_string[i] == 'bot':
                set_bots_later.add(int(in_string[i+1]))
        if 'bot' in in_string[2:]:
            dummy = 123

# Check if both sets are identical.  Since True is printed, both sets are identical.
print(set_bots_start == set_bots_later)
print()

