"""Solutions to https://adventofcode.com/2023/day/14 Puzzles."""
import hashlib
import re
from pathlib import Path

class Parabola():
    
    def __init__(self, control_panel: "list[str]"):
        self.control_panel = control_panel
        self.panel_height = len(self.control_panel)
        self.panel_width = len(self.control_panel[0])

    def print_panel(self):
        for row in self.control_panel:
           print(row) 
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    def shift_north(self): 
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

        self.sort_cols(reverse=True)

    def shift_east(self):
       self.sort_rows() 

    def shift_west(self):
        self.sort_rows(reverse=True)

    def shift_south(self):
        self.sort_cols()

    def sort_rows(self, reverse=False):
        rows = []
        for row in self.control_panel:
            rock_pools = re.findall(r'[^#]+|#', row)
            shifted_row = "".join(["".join(sorted(pool, reverse=reverse)) for pool in rock_pools])
            rows.append(shifted_row)
            
        self.set_control_panel(rows)
    
    def sort_cols(self, reverse=False):
    
        pattern_height = len(self.control_panel)
        pattern_width = len(self.control_panel[0])
        cols = []
        for idx in range(pattern_width):
            col = [self.control_panel[row][idx] for row in range(pattern_height)]
            col = "".join(map(str, col))
        
            rock_pools = re.findall(r'[^#]+|#', col)
            shifted_col = "".join(["".join(sorted(pool, reverse=reverse)) for pool in rock_pools])
            cols.append(shifted_col)
            
        panel = self.rotate_panel(cols)
        self.set_control_panel(panel)

    def rotate_panel(self, panel):
        rotated_panel = []
        for row in panel:
            for x, char in enumerate(row):
                if x == len(rotated_panel):
                    rotated_panel.append(char)
                else:
                    rotated_panel[x] = f"{rotated_panel[x]}{char}"
        return rotated_panel
    def set_control_panel(self, settings):
        self.control_panel = settings

    def calc_north_load(self):
        sum_north_load = 0
        for y, row in enumerate(self.control_panel):
            for x in row:
                if x == "O":
                    sum_north_load += self.panel_height - y
        return sum_north_load 
    
    def calc_load(self, x, n):
        return x*n - (n * (n - 1)) // 2
    
    def get_hash(self, panel):
        hash_object = hashlib.sha256(''.join(panel).encode())
        hash_value = hash_object.hexdigest()[:8]
        return hash_value

    def spin_cycle(self, spin_cycle=1):
        panel_memory = {}
        cycle_memory = {}
        for cycle in range(1, spin_cycle +1):
            panel_memory_before = len(cycle_memory)
            self.shift_north()
            self.shift_west()
            self.shift_south()
            self.shift_east()
            panel_after_cycle = self.control_panel
            cycle_hash = self.get_hash(panel_after_cycle)
            if cycle_hash not in cycle_memory.keys():
                cycle_memory[cycle_hash] = cycle
                panel_memory[cycle] = self.control_panel
            panel_memory_after = len(cycle_memory)
            
            if panel_memory_before == panel_memory_after:
                cycle_start = list(cycle_memory.keys()).index(cycle_hash)
                cycle_length = (len(cycle_memory) - cycle_start)
                last_cycle_offset = (spin_cycle - cycle_start) % cycle_length
                cycle_idx = cycle_start + last_cycle_offset
                last_cycle_panel = panel_memory[cycle_idx]
                self.control_panel = last_cycle_panel
                break

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        parabola = Parabola(puzzle_input)
        parabola.shift_north()
        print(f"Solution to first problem: {parabola.calc_north_load()}")
        
        parabola = Parabola(puzzle_input)
        parabola.spin_cycle(1000000000)
        print(f"Solution to second problem: {parabola.calc_north_load()}")
        
