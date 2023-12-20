# %%
import re
from pathlib import Path
from collections import namedtuple
import sys

class FlipFlop():
    def __init__(self, name, logic, next_name):
        self.name = name
        self.logic = logic
        self.next_name = next_name
        self.state = False
    
    def apply(self, input):
        if input == False:
            self.state = not self.state    
            if self.state:
                return True
            else:
                return False
        else:
            # input == True:
            return None
    
class Conjunction():
    def __init__(self, inputs):
        self.inputs = inputs
    
    def apply(self):
        if all([input.state for input in self.inputs]):
            return False
        else:
            return True

class PulseLogic():
    def __init__(self, puzzle_input: "list[str]"):

        self.broadcast = puzzle_input[0][len("broadcaster ->"):].split()
        print(self.broadcast)
        logic_pattern = re.compile(r"([%&])*(\w+) -> (\w+)")
        self.logic_list = []
        for logic_line in puzzle_input[1:]:
            logic = logic_pattern.search(logic_line)
            logic = Logic(logic.group(1), logic.group(2), logic.group(3))
            self.logic_list.append(logic)
        print(self.logic_list)
        
    
    def pulse_count(self):

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        pulse_logic = PulseLogic(puzzle_input)
        pulse_logic.sort_parts()
        rating = pulse_logic.sum_part_ratings()
        print(f"Solution to first problem: {rating}")
        print(f"Solution to second problem: {pulse_logic.distinct_ratings()}")
        