from pathlib import Path
import re

class Sonar():
    def __init__(self, puzzle_input: "list[str]"):
        self.values = puzzle_input

    def count_larger_than_prev(self, array_size=1):
        sum_of_values = [sum([int(v) for v in self.values[i-array_size:i]]) for i in range(array_size,len(self.values)+1,1)]
        values_larger_than_prev = [int(int(sum_of_values[i - 1]) < int(x)) for i, x in enumerate(sum_of_values) if i > 0]
        return sum(values_larger_than_prev)
        
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        sonar = Sonar(puzzle_input)
        print(f"Solution to first problem: {sonar.count_larger_than_prev()}")
        print(f"Solution to second problem: {sonar.count_larger_than_prev(array_size=3)}")