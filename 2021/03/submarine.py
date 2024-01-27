from pathlib import Path
from collections import namedtuple

Vector = namedtuple("Vector", ["x", "y"])

class Submarine():
    def __init__(self, puzzle_input: "list[str]"):
        self.diagnostic_report = [list(line) for line in puzzle_input]
        self.report_width, self.report_height = len(self.diagnostic_report[0]), len(self.diagnostic_report)

    def get_power_consumption(self):
        gamma, epsilon = 0,0 
        for x in range(self.report_width):
            bin_values = [row[::-1][x] for row in self.diagnostic_report]
            gamma_digit = int(bin_values.count("1") > self.report_height//2)
            gamma += gamma_digit*2**x
            epsilon += (1-gamma_digit)*2**x

        return gamma * epsilon

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        submarine = Submarine(puzzle_input)
        print(f"Solution to first problem: {submarine.get_power_consumption()}")