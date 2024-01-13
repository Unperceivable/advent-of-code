# %%
import re
from pathlib import Path
from collections import namedtuple

class FallingSand():
    def __init__(self, puzzle_input: "list[str]", floor=False):
        self.cave = self.lay_rocks(puzzle_input, floor)
    
    def lay_rocks(self, puzzle_input, floor):
        all_values = []
        x_values, y_values = [],[]
        num_pattern = re.compile(r"(\d+)")
        for line in puzzle_input:
            values = [int(val) for val in num_pattern.findall(line)]
            xv,yv = values[0::2],values[1::2]
            x_values.extend(xv)
            y_values.extend(yv)
            all_values.append([xv,yv])
        min_x = min(x_values)
        x_values = [val-min_x for val in x_values]
        self.cave_width, self.cave_height = max(x_values)+1, max(y_values)+1
        all_values = [[[_-min_x for _ in x], y] for x,y in all_values]
        if floor:
            self.cave_height += 2
            new_width = self.cave_height*2 + 1
            width_diff = new_width - self.cave_width 
            self.cave_width = new_width
            padding = width_diff//2
            min_x -= padding
            all_values = [[[_+padding for _ in x], y] for x,y in all_values]
            floor = [[0,self.cave_width-1],[self.cave_height-1, self.cave_height-1]]
            all_values.append(floor)    
        self.sand_source = (500-min_x, 0)
        
        cave = [[0 for _x in range(self.cave_width)] for _y in range(self.cave_height)]
        
        for x_values, y_values in all_values:
            for idx, (x,y) in enumerate(zip(x_values[1:],y_values[1:]), start=1):
                px = x_values[idx-1]
                py = y_values[idx-1]
                diff_x =  x - px
                diff_y = y - py
                dx,dy = 1,1
                if diff_x:
                    dx = diff_x//abs(diff_x)
                if diff_y:
                    dy = diff_y//abs(diff_y)
                
                for i in range(0,abs(diff_x)+1):
                    cave[py][px+i*dx] = 1
                for i in range(0, abs(diff_y)+1):
                    cave[py+i*dy][px] = 1
        
        return cave

    def print(self):
        _map = {0:".",1:"#",2:"o"}
        for row in self.cave:
            print("".join([_map[c] for c in row]))

    def max_sand(self):
        grain_count = 0
        prev_grain = self.sand_source
        try:
            while True and self.not_blocked(prev_grain, grain_count):
                next_grain = self.sand_source
                prev_grain = self.drop_grain(next_grain)
                grain_count += 1
        except IndexError:
            pass
        return grain_count
    
    def drop_grain(self, pos):
        while not self.stopped_falling(pos): 
            x,y = pos
            if self.on_solid_ground(pos):
                self.cave[y][x] = 2
            else:
                moves = [(x, y+1),(x-1,y+1),(x+1,y+1),]
                for move in moves:
                    _x,_y = move
                    if self.cave[_y][_x] == 0:
                        pos = move
                        break
        return pos
    
    def on_solid_ground(self, pos):
        x,y = pos
        solid_ground = self.cave[y+1][x] != 0
        current_empty = self.cave[y][x] == 0
        left_blocked = self.cave[y+1][x-1] !=0
        right_blocked = self.cave[y+1][x+1] != 0
        return solid_ground and current_empty and left_blocked and right_blocked

    def stopped_falling(self, pos):
        x,y = pos
        return self.cave[y][x] == 2
    
    def not_outbound(self, pos):
        return type(pos) != IndexError
    
    def not_blocked(self, pos, grain_count):
        y = pos[1]
        sy = self.sand_source[1]
        not_blocked = (y != sy) or (not grain_count)
        return not_blocked
    
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        falling_sand = FallingSand(puzzle_input)
        print(f"Solution to first problem: {falling_sand.max_sand()}")
        falling_sand = FallingSand(puzzle_input, floor=True)
        print(f"Solution to second problem: {falling_sand.max_sand()}")