# adventOfCode 2016 day 4
# https://adventofcode.com/20xy/day/4


from collections import Counter

def decrypt_room_name(encrypted_room_name, sectorID):
    encrypted_room_name_dashes2spaces = encrypted_room_name.replace('-', ' ')
    decrypted_room_name_list = []
    for ch in encrypted_room_name_dashes2spaces:
        if ch.islower():
            new_char_num = (ord(ch) + sectorID - ord('a')) % (ord('z') - ord('a') + 1) + ord('a')
            decrypted_room_name_list.append(chr(new_char_num))
        else:
            decrypted_room_name_list.append(ch)
    return ''.join(decrypted_room_name_list)

sum_sectorIDs_realRooms = 0

# Reading input from the input file
input_filename='input_sample1.txt'
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

        sectorID_int = int(sectorID_list)
        sum_sectorIDs_realRooms += sectorID_int
        decrypted_line = decrypt_room_name(line_except_checksum, sectorID_int)
        # accomodate sample scenario or the true (graded) scenario
        if ('encrypted' in decrypted_line) or ('north' in decrypted_line):
            decrypted_room_name = decrypted_line

print(f'The answer to part A is {sum_sectorIDs_realRooms}\n')
print(f'The answer to part B is at the end of the next line \n{decrypted_room_name}\n')

