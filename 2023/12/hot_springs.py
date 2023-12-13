"""Solutions to https://adventofcode.com/2023/day/12 Puzzles."""

from pathlib import Path

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
        
        sum_of_arangements = 0
        for line in self.damage_report:
            visual_report, numeric_report = line.split()
            numeric_report = [int(str) for str in numeric_report.split(",")]
            all_arrangements = self.generate_arrangements(visual_report)
            valid_arrangements = [1 for arranagement in all_arrangements if arranagement == numeric_report]
            sum_of_arangements += sum(valid_arrangements) 
        return sum_of_arangements
    
    def generate_arrangements(self, line):
        arrangements = [line]
        while "?" in arrangements[0]:
            new_arrangements = []
            for line in arrangements:
                new_arrangements.append(line.replace("?", "#", 1))
                new_arrangements.append(line.replace("?", ".", 1))
            arrangements = new_arrangements

        arrangements = [arrangement.split(".") for arrangement in arrangements]
        arrangement_lens = []
        for arrangement in arrangements:
            arrangement_lens.append([len(str) for str in arrangement if str])
        return arrangement_lens

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:
        puzzle_input = puzzle_input_file.read().splitlines()
        print(f"Solution to first problem: {HotSprings(puzzle_input).sum_of_arrangements()}")
        # print(f"Solution to second problem: {HotSprings(puzzle_input).sum_of_arrangements()}")