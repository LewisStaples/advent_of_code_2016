# adventOfCode 2016 day 10
# https://adventofcode.com/2016/day/10

# from dataclasses import dataclass
from enum import Enum
from dataclasses import dataclass
from abc import ABC
import sys


class DestinationType(Enum):
    bot = 0,
    output = 1

class Destination(ABC):
    pass

@dataclass
class Output(Destination):
    def __init__(self):
        self.values = set()


@dataclass
class Bot(Destination):
    def __init__(self, rule_input_list):
        self.values = set()
        self.bot_number = int(rule_input_list[1])
        # print(rule_input_list)

        # low rule
        i_low = rule_input_list.index('low')
        self.low = {'dest_number': int(rule_input_list[i_low+3]), 'dest_type': DestinationType[rule_input_list[i_low+2]]}

        # high rule
        i_high = rule_input_list.index('high')
        self.high = {'dest_number': int(rule_input_list[i_high+3]), 'dest_type': DestinationType[rule_input_list[i_high+2]]}

        # Rule out edge case
        if self.low['dest_number'] == self.high['dest_number']:
            if self.low['dest_type'] == self.high['dest_type'] == DestinationType.bot:
                ValueError('Edge case:  we cannot have a bot sending both chips to the same [other] bot')



    def add_value(self, value):
        self.values.add(value)
        if 17 in self.values and 61 in self.values:
            print(f'The answer to part A is {self.bot_number}')
            sys.exit('Program Complete')
    
    def get_number_of_bots(self):
        return len(self.values)

    def remove_bots(self):
        if len(self.values) < 2:
            raise ValueError('not enough robots!')
        low_val, high_val = min(self.values), max(self.values)
        self.values = set()
        return {'low': (low_val, self.low['dest_type'], self.low['dest_number']), 
        'high': (high_val, self.high['dest_type'], self.high['dest_number'])}
        

@dataclass
class OutputBin:
    def __init__(self):
        self.values = set()


# (not referring to facility as a "factory," less someone thinks I am referring to the factory design pattern)
class MicrochipFacility:
    def __init__(self):
        self.bots = dict()
        self.outputs = dict()
        self.initial_chip_locations = []

        # Reading input from the input file
        input_filename='input_sample0.txt'
        print(f'\nUsing input file: {input_filename}\n')
        with open(input_filename) as f:
            # Pull in each line from the input file
            for in_string in f:
                in_string = in_string.rstrip()
                self.process_input_line(in_string)

    
    def process_input_line(self, in_string):
        # print(in_string)
        in_string_list = in_string.split(' ')

        # Transfer from "input" bin to a bot
        if in_string_list[0] == 'value':
            # assert in_string_list[4] == 'bot'
            self.initial_chip_locations.append(
                (int(in_string_list[1]), 
                DestinationType[(in_string_list[4])], 
                int(in_string_list[5]))
            )
            
            # print(in_string)

        # Record the rules for what to do when two items are in this bot
        elif in_string_list[0] == 'bot':
            self.bots[int(in_string_list[1])] = Bot(in_string_list)
        else:
            raise ValueError('Bad input line: ' + in_string)

    def start_transfers(self):
        # Place chips in initial bot locations
        for bot_loc in self.initial_chip_locations:
            self.transfer_value(None, bot_loc)


        while True:
            for bot_num in self.bots:
                if len(self.bots[bot_num].values) == 2:
                    # Verify that there is space to transfer the bots to
                    if self.bots[bot_num].low['dest_type'] == DestinationType.bot:
                        if len(self.bots[
                            self.bots[bot_num].low['dest_number']
                        ].values) >= 2:
                            continue
                    if self.bots[bot_num].high['dest_type'] == DestinationType.bot:
                        if len(self.bots[
                            self.bots[bot_num].high['dest_number']
                        ].values) >= 2:
                            continue

                #     # Transfer the bots: low and then high
                #     self.transfer_value((min(self.bots.values), DestinationType.bot, self.bots[bot_num].low['dest_number']), 
                #     (self.bots.values[0], DestinationType.bot, self.bots[bot_num].high['dest_number']))
                #     break

                # elif len(self.bot[bot_num]) > 2:
                #     raise ValueError(f'Bot # {bot_num} has more than two chips!!!')

            # This should only happen if no record triggered a break from the for loop
            break

    def transfer_value(self, old_chiploc, new_chiploc):
        if old_chiploc is not None:
            old_chip_value = old_chiploc[0]
            old_dest_num = old_chiploc[2]

            # You can't transfer chips out of any output !!!
            if old_chiploc[1] != DestinationType.bot:
                raise ValueError('Bad Old LocationType: ' + old_chiploc[1])




            self.bots[old_dest_num].values.remove(old_chip_value)

        new_chip_value = new_chiploc[0]
        new_dest_num = new_chiploc[2]

        if new_chiploc[1] == DestinationType.bot:
            self.bots[new_dest_num].add_value(new_chip_value)
        else:
            if new_dest_num in self.outputs:
                self.outputs[new_dest_num].append(new_chip_value)
            else:
                self.outputs[new_dest_num] = [new_chip_value]


    # def transfer_value_to(self):
    #     pass

    # def transfer_value_from(self):
    #     pass

microchipfacility = MicrochipFacility()
microchipfacility.start_transfers()

dummy = 123

