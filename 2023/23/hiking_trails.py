# %%
from pathlib import Path
from collections import namedtuple
import sys

sys.setrecursionlimit(100000)

Coord = namedtuple("Coord", ["x", "y"])
from copy import copy
class HikingTrails():
    
    def __init__(self, puzzle_input: "list[str]"):
        self.trail = [list(row) for row in puzzle_input]
        self.trail_legend = {"path":".", "forest":"#", "up_slope":"^", "right_slope":">", "down_slope":"v", "left_slope": "<"}

        self.trail_width = len(self.trail[0])
        self.trail_height = len(self.trail)

        self.trail_start = Coord(self.trail[0].index(self.trail_legend["path"]), 0)
        self.trail_end = Coord(self.trail[-1].index(self.trail_legend["path"]), self.trail_height-1)
        self.paths = []
        self.get_paths(self.trail_start, self.trail)


    def get_if_valid_path(self, pos, trail):
        in_trail =  0 <= pos.y < self.trail_height and 0 <= pos.x < self.trail_width
        if in_trail:
            current_step_type = trail[pos.y][pos.x]
            in_trail = current_step_type not in [self.trail_legend["forest"], "X"]

        if in_trail:
            return pos

    def get_paths(self, pos, trail, num_steps=-1):
    
        go_right = Coord(pos.x + 1, pos.y)
        go_left = Coord(pos.x - 1, pos.y)
        go_down = Coord(pos.x, pos.y + 1)
        go_up = Coord(pos.x, pos.y - 1)
        
        current_step_type = trail[pos.y][pos.x]
        trail[pos.y][pos.x] = "X"
        num_steps += 1

        if pos.x == self.trail_end.x and pos.y == self.trail_end.y:
            self.paths.append(num_steps)
        
        else:

            next_pos = []
            
            if current_step_type == self.trail_legend["path"]:
                next_pos = [go_right, go_left, go_down, go_up]
            elif current_step_type == self.trail_legend["up_slope"]:
                next_pos = [go_up]
            elif current_step_type == self.trail_legend["down_slope"]:
                next_pos = [go_down]
            elif current_step_type == self.trail_legend["left_slope"]:
                next_pos = [go_left]
            elif current_step_type == self.trail_legend["right_slope"]:
                next_pos = [go_right]
            
            next_pos = [self.get_if_valid_path(p, trail) for p in next_pos]
            next_pos = [pos for pos in next_pos if pos]
            
            for pos in next_pos:
                new_trail = [row[:] for row in trail]
                self.get_paths(pos, new_trail, num_steps)

        
        
    def longest_path(self):
        return max(self.paths)
    
    def print_trail(self, trail):
        print("|||||||||||||||||||||||||||||||||||")
        for row in trail:
            print("".join(row))   
        print("|||||||||||||||||||||||||||||||||||")
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        hiking_trails = HikingTrails(puzzle_input)
        print(f"Solutions to first problem: {hiking_trails.longest_path()}")
        # print(f"Solution to second problem: {hiking_trails.distinct_ratings()}")