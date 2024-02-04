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

        self.completion_score = {"(": 1,
                                 "[": 2,
                                 "{": 3,
                                 "<": 4,}
        
        self.matching_brackets = {")": "(",
                             "]": "[",
                             "}": "{",
                             ">": "<",}
        self.check_syntax()
    
    def check_syntax(self):
        self.error_count = {bracket:0 for bracket in self.error_severity.keys()}
        self.leftover_brackets = []
        for line in self.lines:
            stack = []
            corrupted = False
            for pos, char in enumerate(line):
                if char in self.error_count.keys():
                    last_bracket = stack.pop()
                    if last_bracket != self.matching_brackets[char]:
                        self.error_count[char] += 1
                        corrupted = True
                else:
                    stack.append(char)
            if not corrupted:
                self.leftover_brackets.append(stack)

    def get_completion_score(self):
        completion_scores = []
        for line in self.leftover_brackets:
            line_score = [self.completion_score[b] for b in line][::-1]
            completion_score = 0
            for score in line_score:
                completion_score *= 5
                completion_score += score 
            completion_scores.append(completion_score)
        median_score = np.median(np.array(completion_scores))
        return int(median_score)

    def get_error_score(self):
        error_score = sum(self.error_count[bracket]*self.error_severity[bracket] for bracket in self.error_count.keys())
        return error_score
        
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        syntax_check = SyntaxCheck(puzzle_input)
        print(f"Solution to first problem: {syntax_check.get_error_score()}")
        print(f"Solution to second problem: {syntax_check.get_completion_score()}")