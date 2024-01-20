# %%
from pathlib import Path
from collections import namedtuple
import re

Coord = namedtuple("Coord", ["x", "y", "z"])

class Monkey():
    def __init__(self, puzzle_input: "list[str]"):
        self.values = self.get_values(puzzle_input)

    def get_values(self, puzzle_input):
        values = {}
        for line in puzzle_input:
            monkey, value = line.split(": ")
            values[monkey]=f"({value})" 
        return values
    
    
    def root_value(self):
        root_value = self.values["root"]
        variables  = self.get_variables(root_value)
        while variables:
            for var in variables:
                root_value = root_value.replace(var, self.values[var])
            variables = self.get_variables(root_value)
        root_value = eval(root_value)
        return int(root_value)
    
    def get_variables(self, value):
        str_pattern = re.compile(r"([a-z]+)")
        variables = str_pattern.findall(value)
        return variables
    
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        monkey = Monkey(puzzle_input)
        print(f"Solution to first problem: {monkey.root_value()}")