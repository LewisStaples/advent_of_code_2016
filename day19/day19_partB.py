# adventOfCode 2016 day 19
# https://adventofcode.com/2016/day/19


from dataclasses import dataclass
import time
from datetime import timedelta


@dataclass
class Elf:
    elf_number: int
    number_presents: int = 1


start_time = time.monotonic()


# Reading input from the input file
input_filename='input.txt'

with open(input_filename) as f:
    in_string = f.readline().rstrip()
print(f'\nUsing input file: {input_filename}, which indicates there are {in_string} elves.\n')

# Initializations
ELF_COUNT = int(in_string)
del in_string
elf_present = [Elf(x+1) for x in range(ELF_COUNT)]
receiver_elf_index = 0

# Start looping through all elves
while True:
    # Transfer presents from giver to receiver elf 
    giver_elf_index = (receiver_elf_index + len(elf_present)//2) % len(elf_present)
    elf_present[receiver_elf_index].number_presents += elf_present[giver_elf_index].number_presents
    # Test if complete
    if elf_present[receiver_elf_index].number_presents == ELF_COUNT:
        break
    # Remove the elf who gave up all their presents
    del elf_present[giver_elf_index]

    # Determine the next elf index
    if giver_elf_index > receiver_elf_index:
        receiver_elf_index += 1
    receiver_elf_index %= len(elf_present)

print(f'Elf number # {elf_present[receiver_elf_index].elf_number} is the one that gets all of the presents (This is the answer to Part B)\n')

# Note run time is 
end_time = time.monotonic()
print(f'Time for program to run (hr:min:sec): {timedelta(seconds=end_time - start_time)}')

