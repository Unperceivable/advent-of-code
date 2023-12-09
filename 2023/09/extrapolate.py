"""Solutions to https://adventofcode.com/2023/day/9 Puzzles."""
import math
import re
from pathlib import Path

 
def extrapolate(sensor_input: "list[str]", reverse=False):
    """Returns sum of extrapolated values

    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    
    Extrapolate values by finding the consecutive differences.
    Sum of these extrapolated values is 114 for this example."""

    def diff(vals):
        "Return list of differences between list of values"
        diff_values = [v2-v1 for v1,v2 in zip(vals[:-1],vals[1:])]
        return diff_values

    sum_of_extrapolation = 0
    for line in sensor_input:
        values = line.split()
        if reverse:
            values.reverse()    
        value_history = [[int(val) for val in values]]
        while sum(value_history[-1]) != 0:
            value_history.append(diff(value_history[-1]))
        sum_of_extrapolation += sum([value_history[i][-1] for i in range(len(value_history))])
    
    return sum_of_extrapolation


if __name__ == "__main__":    
    puzzle_input_path = Path("readings.txt")
    with open(puzzle_input_path) as puzzle_input_file:
        puzzle_input = puzzle_input_file.read().splitlines()
        print(f"Sum of extrapolation: {extrapolate(puzzle_input)}")
        print(f"Sum of reverse extrapolation: {extrapolate(puzzle_input, reverse=True)}")