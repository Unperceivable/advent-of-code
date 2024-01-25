from pathlib import Path
import re

class Sonar():
    def __init__(self, puzzle_input: "list[str]"):
        self.count_larger_than_prev_value = self.count_larger_than_prev(puzzle_input)

    def count_larger_than_prev(self, values):
        values = [int(int(values[i - 1]) < int(x)) for i, x in enumerate(values) if i > 0]
        return sum(values)
    
        
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        sonar = Sonar(puzzle_input)
        print(f"Solution to first problem: {sonar.count_larger_than_prev_value}")