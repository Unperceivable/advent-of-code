# %% 
"""Solutions to https://adventofcode.com/2023/day/14 Puzzles."""
import re
from pathlib import Path

class Parabola():
    
    def __init__(self, control_panel: "list[str]"):
        self.control_panel = control_panel
        self.panel_height = len(self.control_panel)
        self.panel_width = len(self.control_panel[0])
        self.spin_cycle = 1000000000

    def north_total_load(self): 
        """Return total load on parabola if all rocks are north.

        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....

        Move all rocks as north as possible where, O will roll, # stay in place. . are empty spaces
        Ca1culate the sum of all distances to the bottom of the controls for each rock, in this case 136"""
            
        pattern_height = len(self.control_panel)
        pattern_width = len(self.control_panel[0])
        sum_of_loads = 0
        for idx in range(pattern_width):
            col = [self.control_panel[row][idx] for row in range(pattern_height)]
            col = "".join(map(str, col))
        
            stop_pattern = re.compile(r"#*")
            stop_matches = stop_pattern.finditer(col)
            stop_spans = [match.span() for match in stop_matches if match.group()] 
            start = 0
            rock_pools = [pool for pool in col.split("#") if pool]
            idx_shift = 0
            if stop_spans and stop_spans[0][0] == 0:
                start = stop_spans[0][1]
                idx_shift = 1
            
            col_str = {}
            for idx, pool in enumerate(rock_pools):
                pool_start = pattern_height-start
                pool_str = pool.count("O")
                col_str[pool_start] = pool_str
                load = self.calc_load(pool_start, pool_str)
                sum_of_loads += load
                if  len(stop_spans) > idx+idx_shift :
                    start = stop_spans[idx+idx_shift][1]
        return sum_of_loads 

    def set_control_panel(self, settings):
        self.control_panel = settings

    def calc_north_load(self):
        for y, row in enumerate(self.control_panel):
            for x in row:
                if x == "O":
                    return self.panel_height - y
                else:
                    return 0
        return
    
    def calc_load(self, x, n):
        return x*n - (n * (n - 1)) // 2
    
     
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        parabola = Parabola(puzzle_input)
        print(f"Solution to first problem: {parabola.north_total_load()}")
        # print(f"Solution to second problem: {parabola.north_total_load(spin_cycle=True)}")
        
