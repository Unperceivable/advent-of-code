"""Solutions to https://adventofcode.com/2023/day/12 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path
from itertools import combinations

Coord = namedtuple("Coord", ["x", "y"])

class HotSprings():
    
    def __init__(self, damage_report: "list[str]"):
        self.damage_report = damage_report

    def sum_of_arrangements(self):
        """Returns sum of possible arrangements based on damage_report.
        
        ???.### 1,1,3
        .??..??...?##. 1,1,3
        ?#?#?#?#?#?#?#? 1,3,1,6
        ????.#...#... 4,1,1
        ????.######..#####. 1,6,5
        ?###???????? 3,2,1
        
        visual: operational (.), damaged (#) or unknown (?) 
        numeric: describes portions of consecutive damage
        Return the sum of arrangements posible due to the unkown portions, in this case 10 (1,4,1,4,10)"""
        
        
        for line in self.damage_report:
            visual_report, numeric_report = line.split
            numeric_report = numeric_report.split(",")
            base_pattern = "[.?]*?([?#]{" + numeric_report[0]+ "})"
            pattern_prefix = "[.?]+?([?#]{"
            pattern_postfix = "})"
            rest_pattern = "".join([rf"{pattern_prefix}{val}{pattern_postfix}" for val in numeric_report[1:]])
            arrangement_pattern =  f"(?={base_pattern}{rest_pattern})"
            print(arrangement_pattern)
            arrangement_pattern = re.compile(arrangement_pattern)
            arrangements = arrangement_pattern.findall(visual_report)
            print(arrangements)
            print(len(arrangements))

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        print(f"Solution to first problem: {HotSprings(puzzle_input).sum_of_arrangements()}")
        print(f"Solution to second problem: {HotSprings(puzzle_input).sum_of_arrangements()}")