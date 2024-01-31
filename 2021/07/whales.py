from pathlib import Path

import numpy as np

class Whales():
    def __init__(self, puzzle_input: "list[str]"):
        self.positions = np.array([int(f) for f in puzzle_input[0].split(",")], dtype=np.int32)

    def get_fuel_spent(self):
        median =  np.median(self.positions)
        self.positions -= int(median)
        fuel_spent = np.absolute(self.positions)
        return np.sum(fuel_spent)
            

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        whale = Whales(puzzle_input)
        print(f"Solution to first problem: {whale.get_fuel_spent()}")