# %%
import re
from pathlib import Path
from collections import namedtuple
import sys

class StepCounter():
    def __init__(self, puzzle_input: "list[str]"):
        self.garden_tiles = {"plot": ".", "stone": "#", "start":"S", "passed":"X"}

        self.garden = [list(row) for row in puzzle_input]
        self.garden_width = len(puzzle_input[0])
        self.garden_height = len(puzzle_input)
        self.start = self.get_start_point(self.garden)
        self.expanded_garden = 3*[list(3*"".join(row)) for row in self.garden]
        self.exp_garden_width = len(self.expanded_garden[0])
        self.exp_garden_height = len(self.expanded_garden)
        print((self.exp_garden_width, self.exp_garden_height))
        self.step_map()
        
    def step_map(self):
        reachable_plots = [(15,15)]
        garden_width = self.exp_garden_width
        garden_height = self.exp_garden_height
        garden = self.expanded_garden
        dist_map = [["0" for _ in range(garden_width)] for _ in range(garden_height)]
        for step in range(50):
            new_plots = []
            # print(reachable_plots)
            for ox, oy in reachable_plots:
                # print((ox,oy))
                adj_plots = [(ox + 1, oy),
                    (ox - 1, oy),
                    (ox, oy + 1),
                    (ox, oy - 1),]
                for x,y in adj_plots:
                    in_garden =  0 <= y < garden_height and 0 <= x < garden_width
                    is_reachable = in_garden and garden[y][x] in [self.garden_tiles["plot"], self.garden_tiles["start"]]
                    # print((x,y, in_garden, is_reachable))
                    if is_reachable:
                        new_plots.append((x,y))
                        if dist_map[y][x] == "0":
                            dist_map[y][x] = f"{step}"
            reachable_plots = list(set(new_plots))

        self.print_garden(dist_map)
        return len(reachable_plots)
    
    def print_garden(self, garden=None):
        import matplotlib.pyplot as plt
        import numpy as np
        if not garden:
            garden = self.garden
        garden = np.array(garden, dtype=float) 
        data_array = np.array(garden)
        plt.imshow(data_array, cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.show()
    
    def get_start_point(self, garden):
        if not garden:
            garden = self.garden
        for y, row in enumerate(garden):
            try:
                x = row.index(self.garden_tiles["start"])
                if x:
                    return (x, y)  
            except ValueError:
                pass
    
    def max_steps(self):
        prev_max = -1
        max = 0        
        max_steps = 0
        while prev_max >= max:
            max_steps +=1
            prev_max = max_steps
            num_plots = self.reachable_plots(max_steps)
            max = max(max_steps, num_plots)
            print(num_plots)
            print(prev_max > max)
        
        return max_steps 
    
    def reachable_plots(self, steps=50, start=None):
        if not start:
            start=self.start
        reachable_plots = [start]
        
        for _ in range(steps):
            new_plots = []
            # print(reachable_plots)
            for ox, oy in reachable_plots:
                # print((ox,oy))
                self.print_garden()
                adj_plots = [(ox + 1, oy),
                    (ox - 1, oy),
                    (ox, oy + 1),
                    (ox, oy - 1),]
                for x,y in adj_plots:
                    in_garden =  0 <= y < self.garden_height and 0 <= x < self.garden_width
                    is_reachable = in_garden and self.garden[y][x] in [self.garden_tiles["plot"], self.garden_tiles["start"]]
                    # print((x,y, in_garden, is_reachable))
                    if is_reachable:
                        new_plots.append((x,y))
            reachable_plots = list(set(new_plots))

        return len(reachable_plots)
    
    def total_plots(self):
        stones = 0
        for row in self.garden:
            stones += row.count(self.garden_tiles["stone"])
        total_tiles = self.garden_width*self.garden_height
        return total_tiles - stones

    def max_plots(self):

        max_plots = 0
        total_plots = self.total_plots()
        print(total_plots)
        if total_plots % 2:
            max_plots = total_plots // 2 + 2
        else:
            max_plots = total_plots // 2        
    
        return max_plots 

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        step_counter = StepCounter(puzzle_input)
        num_plots = step_counter.reachable_plots(steps=64)
        print(f"Solution to first problem: {num_plots}")
        # print(f"Solution to second problem: {step_counter.distinct_ratings()}")
        