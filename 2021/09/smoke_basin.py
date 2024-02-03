from pathlib import Path

import numpy as np

class SmokeBasin():
    def __init__(self, puzzle_input: "list[str]"):
        pass

    def get_risk_level(self):
        return 0 

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        whale = SmokeBasin(puzzle_input)
        print(f"Solution to first problem: {whale.get_risk_level()}")