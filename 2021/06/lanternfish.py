from pathlib import Path
from collections import namedtuple

import numpy as np

class Lanternfish():
    def __init__(self, puzzle_input: "list[str]"):
        self.school = np.array([int(f) for f in puzzle_input[0].split(",")])

    def get_school_size(self, days=80):
        for _ in range(days):
            # count num 0 dead fish
            num_dead_fish = np.count_nonzero(self.school == 0)
            self.school[self.school==0] +=7
            self.school = np.concatenate([self.school, np.array(num_dead_fish*[9], dtype=np.int32)])
            self.school -= 1
            # decrease fish age
        return self.school.shape[0]
    


            

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        lanternfish = Lanternfish(puzzle_input)
        print(f"Solution to first problem: {lanternfish.get_school_size(days=80)}")