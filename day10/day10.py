# adventOfCode 2016 day 10
# https://adventofcode.com/2016/day/10


from enum import Enum

class DestinationType(Enum):
    bot = 0,
    output = 1


class Bot:
    def __init__(self, rule_input_list):
        self._values = set()
        self.bot_number = int(rule_input_list[1])

        # create low rule
        i_low = rule_input_list.index('low')
        self.low_rule = {'dest_number': int(rule_input_list[i_low+3]), 'dest_type': DestinationType[rule_input_list[i_low+2]]}

        # create high rule
        i_high = rule_input_list.index('high')
        self.high_rule = {'dest_number': int(rule_input_list[i_high+3]), 'dest_type': DestinationType[rule_input_list[i_high+2]]}


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

        # Now, traverse self.initial_chip_locations
        for value_num, bot_num in self.initial_chip_locations:
            self.bots[bot_num]._values.add(value_num)

    def add_value(self, dest_num, dest_type, value_num):
        if dest_type == DestinationType.output:
            if dest_num not in self.outputs:
                self.outputs[dest_num] = [value_num]
                return

        assert len(self.bots[dest_num]._values) < 2
        self.bots[dest_num]._values.add(value_num)


    def transfer_chips(self, bot_num):
        assert len(self.bots[bot_num]._values) <= 2

        # Verify that the starting bot has two chips
        if len(self.bots[bot_num]._values) < 2:
            return 0

        # Look for part A answer:
        if self.bots[bot_num]._values == {17, 61}:
            print(f'The answer to part A is bot # {bot_num}\n')


        low_dest_num = self.bots[bot_num].low_rule['dest_number']
        high_dest_num = self.bots[bot_num].high_rule['dest_number']
        low_value = min(self.bots[bot_num]._values)
        high_value = max(self.bots[bot_num]._values)

        # If either destination is a bot with two chips, transfer that first
        if self.bots[bot_num].low_rule['dest_type'] == DestinationType.bot:
            if len(self.bots[low_dest_num]._values) == 2:
                self.transfer_chips(self, low_dest_num)
            self.bots[low_dest_num]._values.add(low_value)
        if self.bots[bot_num].high_rule['dest_type'] == DestinationType.bot:
            if len(self.bots[high_dest_num]._values) == 2:
                self.transfer_chips(self, high_dest_num)
            self.bots[high_dest_num]._values.add(high_value)

        if self.bots[bot_num].low_rule['dest_type'] == DestinationType.output:
            if low_dest_num not in self.outputs:
                self.outputs[low_dest_num] = set()
            self.outputs[low_dest_num].add(low_value)
        if self.bots[bot_num].high_rule['dest_type'] == DestinationType.output:
            if high_dest_num not in self.outputs:
                self.outputs[high_dest_num] = set()
            self.outputs[high_dest_num].add(high_value)

        self.bots[bot_num]._values.clear()
        return 1

    def process_input_line(self, in_string):
        in_string_list = in_string.split(' ')

        #  Put record in self.initial_chip_locations
        if in_string_list[0] == 'value':
            assert in_string_list[4] == 'bot'
            self.initial_chip_locations.append(
                (int(in_string_list[1]), 
                int(in_string_list[5]))
            )

        # Record the rules for what to do when two items are in this bot
        elif in_string_list[0] == 'bot':
            self.bots[int(in_string_list[1])] = Bot(in_string_list)
        else:
            # Input lines must start either with "value" or "bot"!
            raise ValueError('Bad input line: ' + in_string)

    def run_facility(self):
        while True:
            ret_val = 0
            for bot_num in self.bots:
                ret_val += self.transfer_chips(bot_num)
            if ret_val == 0:
                # Note that part A is not expected to get this far
                print('All chips have been transferred now')
                partB_soln = self.outputs[0].pop() * self.outputs[1].pop() * self.outputs[2].pop()
                print(f'The solution to part B is {partB_soln}\n')
                return

microchipfacility = MicrochipFacility()
microchipfacility.run_facility()



