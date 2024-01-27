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
    
    def get_life_support_rating(self):
        o_values, co2_values = self.diagnostic_report[:], self.diagnostic_report[:]

        for x in range(self.report_width):
            
            if len(o_values) > 1:
                bin_values = [row[x] for row in o_values]
                highest_bit = 1 - int(bin_values.count("0") > len(o_values)//2)
                o_values = [value for value in o_values if value[x] == str(highest_bit)]

            if len(co2_values) > 1:
                bin_values = [row[x] for row in co2_values]
                lowest_bit = int(bin_values.count("0") > len(co2_values)//2)
                co2_values = [value for value in co2_values if value[x] == str(lowest_bit)]

        o_generator_rating = int("".join(o_values[0]), 2)
        co2_scrubber_rating = int("".join(co2_values[0]), 2)
        return  o_generator_rating * co2_scrubber_rating
    
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        submarine = Submarine(puzzle_input)
        print(f"Solution to first problem: {submarine.get_power_consumption()}")
        print(f"Solution to second problem: {submarine.get_life_support_rating()}")