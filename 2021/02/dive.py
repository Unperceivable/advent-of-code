from pathlib import Path
from collections import namedtuple

Vector = namedtuple("Vector", ["x", "y"])

class Dive():
    def __init__(self, puzzle_input: "list[str]"):
        self.dive_pattern = puzzle_input

    def get_dive_length(self, inverted=False):
        x,y,aim = 0,0,0
        for dive in self.dive_pattern:
            direction, value = dive.split() 
            value = int(value)
            if direction in ["up", "down"]:
                if direction == "up":
                    value = -value
                if inverted:
                    aim += value
                else:
                    y += value
            if "forward" == direction:
                x += value
                if inverted:
                    y += aim*value
        return x*y


if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        dive = Dive(puzzle_input)
        print(f"Solution to first problem: {dive.get_dive_length()}")
        print(f"Solution to second problem: {dive.get_dive_length(inverted=True)}")