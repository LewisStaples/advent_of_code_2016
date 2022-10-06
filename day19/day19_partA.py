# adventOfCode 2016 day 19
# https://adventofcode.com/2016/day/19


from dataclasses import dataclass


@dataclass
class Elf:
    next_elf: int
    number_presents: int = 1


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   
# Initializations
ELF_COUNT = int(in_string)
del in_string
elf_present = {x:Elf(x+1) for x in range(ELF_COUNT)}
elf_present[ELF_COUNT - 1].next_elf = 0
next_elf_index = 0

# Start looping through all elves
while True:
    this_elf_index = next_elf_index
    next_elf_index = elf_present[this_elf_index].next_elf
    if elf_present[this_elf_index].number_presents == 0:
        continue
    elf_present[this_elf_index].number_presents += elf_present[next_elf_index].number_presents
    elf_present[next_elf_index].number_presents = 0 # superfluous
    elf_present[this_elf_index].next_elf = elf_present[next_elf_index].next_elf
    if elf_present[this_elf_index].number_presents == ELF_COUNT:
        break

# The answer is the index plus 1, because the problem statement labels positions starting at 1, but the code's index starts at 0
print(f'Elf number # {this_elf_index + 1} is the one that gets all of the presents (This is the answer to Part A)\n')

