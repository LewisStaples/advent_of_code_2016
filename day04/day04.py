# adventOfCode 2016 day 4
# https://adventofcode.com/20xy/day/4


from collections import Counter

sum_sectorIDs_realRooms = 0

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()

        # Find right-most instances of [ and ] (just in case there are more than one of either)
        checksum_indices = (
            in_string.rfind('[') ,
            in_string.rfind(']')
        )
        checksum = in_string[checksum_indices[0] + 1 : checksum_indices[1]]
        line_except_checksum = in_string[:checksum_indices[0]]
        sectorID_list = ''.join(filter(lambda i: i.isdigit(), line_except_checksum))
        encrypted_name_letters = ''.join(filter(lambda i: i.isalpha(), line_except_checksum))
        del checksum_indices

        the_counter = Counter(encrypted_name_letters).most_common()
        
        fail_flag = False
        for i_ch, ch in enumerate(checksum):
            freq = the_counter[i_ch][1]
            if (ch, freq) not in the_counter:
                # This room is a decoy
                fail_flag = True
                break
        
        # Skip any further use of any decoy rooms:
        if fail_flag == True:
            continue

        sum_sectorIDs_realRooms += int(sectorID_list)

print(f'The answer to part A is {sum_sectorIDs_realRooms}\n')


