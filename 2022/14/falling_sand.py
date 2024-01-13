# %%
import re
from pathlib import Path
from collections import namedtuple

class FallingSand():
    def __init__(self, puzzle_input: "list[str]"):
        self.cave = self.lay_rocks(puzzle_input)
    
    def lay_rocks(self, puzzle_input):
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
        self.sand_source = (500-min_x, 0)
        x_values = [val-min_x for val in x_values]
        all_values = [[[_-min_x for _ in x], y] for x,y in all_values]
        self.cave_width, self.cave_height = max(x_values)+1, max(y_values)+1
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
        while not type(prev_grain) == IndexError:
            next_grain = self.sand_source
            prev_grain = self.drop_grain(next_grain)
            grain_count += 1
        return grain_count - 1
    
    def drop_grain(self, pos):
        try:
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
        except IndexError as e:
            return e

    def on_solid_ground(self, pos):
        x,y = pos
        solid_ground = self.cave[y+1][x] != 0
        current_empty = self.cave[y][x] == 0
        left_blocked = self.cave[y+1][x-1] !=0
        right_blocked = self.cave[y+1][x+1] != 0
        return solid_ground and current_empty and left_blocked and right_blocked

    # def on_sand(self, pos):
    #     x,y = pos
    #     solid_ground = self.cave[y+2][x] == 2
    #     solid_ground = self.cave[y+1][x] == 2
    #     current_empty = self.cave[y][x] == 0
    #     return solid_ground and current_empty
    
    def stopped_falling(self, pos):
        x,y = pos
        return self.cave[y][x] == 2
    
    def in_bounds(self, pos):
        x,y = pos
        in_width = 0 <= x < self.cave_width
        in_height = 0 <= y < self.cave_height
        return in_width and in_height
    
    
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        falling_sand = FallingSand(puzzle_input)
        print(f"Solution to first problem: {falling_sand.max_sand()}")
        # print(f"Solution to second problem ")