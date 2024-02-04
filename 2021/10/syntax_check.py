from pathlib import Path
from collections import namedtuple
import numpy as np

Pos = namedtuple("Pos", ["x", "y"])

class SyntaxCheck():
    def __init__(self, puzzle_input: "list[str]"):
        self.lines = puzzle_input
        self.error_severity = {")": 3,
                               "]": 57,
                               "}": 1197,
                               ">": 25137,}

    def get_error_score(self):
        matching_brackets = {")": "(",
                             "]": "[",
                             "}": "{",
                             ">": "<",}
        error_count = {bracket:0 for bracket in self.error_severity.keys()}
        stack = []
        for line in self.lines:
            # print(f"line: {line}")
            for pos, char in enumerate(line):
                if char in error_count.keys():
                    last_bracket = stack.pop()
                    if last_bracket != matching_brackets[char]:
                        # print(f"out of order {line[:pos]}, {last_bracket}, {char}")
                        error_count[char] += 1
                else:
                    stack.append(char)

        # print(error_count)
        error_score = sum(error_count[bracket]*self.error_severity[bracket] for bracket in error_count.keys())
        return error_score
        
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        syntax_check = SyntaxCheck(puzzle_input)
        print(f"Solution to first problem: {syntax_check.get_error_score()}")