"""Solutions to https://adventofcode.com/2023/day/13 Puzzles."""
from math import floor
from pathlib import Path

class MirrorValley():
    
    def __init__(self, pattern_notes: "list[str]"):
        self.pattern_notes = pattern_notes
        self.pattern_notes.append("")

    def print_pattern(self, pattern):
        for line in pattern:
            print(line)

    def sum_of_reflections(self, smudged=False): 
        """Returns sum of horizontal and vertical reflection strength/positions .
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.
        
        #...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#

        
        Return the sum of all columns left of reflection + 100x number of rows above relfection
        Example Total: 405(5 + 4x100) - First pattern's reflects after 5 columns, second reflects after 4 rows"""
        mirrored_values = []
        pattern = []
        for line in self.pattern_notes:
            if line:
                pattern.append(line)
            else:
                mirrored_value = self.find_horizontal_mirror(pattern, smudged)
                if mirrored_value:
                    mirrored_value *= 100
                else:
                    mirrored_value = self.find_vertical_mirror(pattern, smudged)
                mirrored_values.append(mirrored_value)
                pattern = []
                
        return sum(mirrored_values)    

    def find_horizontal_mirror(self, pattern:"list[str]", smudged: bool):
        pattern_height = len(pattern)
        middle_idx = floor(pattern_height/2)
        for direction in [1,-1]:
            for idx in range(1, middle_idx+1):
                    
                ll_idx = 0
                lr_idx = idx
                rl_idx = idx
                rr_idx = 2*idx

                if direction == -1:
                    ll_idx = idx * direction
                    lr_idx = None
                    rl_idx = 2*idx * direction
                    rr_idx = idx * direction

                rows_left = pattern[ll_idx:lr_idx]
                rows_right = pattern[rl_idx:rr_idx]

                rows_right.reverse()
                
                if self.check_reflection(rows_left, rows_right, smudged):
                    reflection_point = idx
                    if direction == -1:
                       reflection_point = pattern_height - idx
                    return reflection_point
            
    def find_vertical_mirror(self, pattern: "list[str]", smudged: bool):
        pattern_height = len(pattern)
        pattern_width = len(pattern[0])
        vertical_pattern = []
        for idx in range(pattern_width):
            col = [pattern[row][idx] for row in range(pattern_height)]
            col = "".join(map(str, col))
            vertical_pattern.append(col)
        
        return self.find_horizontal_mirror(vertical_pattern, smudged)
        
    def check_reflection(self, rows_left: "list[str]", rows_right: "list[str]", smudged: bool):
        
        if smudged:
            differences = 0
            for str1, str2 in zip(rows_left, rows_right):
                differences += sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)
            return differences == 1

        else:
            return rows_left == rows_right


if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        mirror_valley = MirrorValley(puzzle_input)
        print(f"Solution to first problem: {mirror_valley.sum_of_reflections()}")
        print(f"Solution to second problem: {mirror_valley.sum_of_reflections(smudged=True)}")