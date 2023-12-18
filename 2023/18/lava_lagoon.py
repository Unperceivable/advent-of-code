# %%
"""Solutions to https://adventofcode.com/2023/day/15 Puzzles."""
import re
from pathlib import Path
from collections import namedtuple
import sys

# sys.setrecursionlimit(50000)

class LavaLagoon():
    def __init__(self, dig_plan: "list[str]"):
        self.dig_plan = dig_plan
        self.site_width = 0
        self.site_height = 0
        self.dig_site =  [[]]   
        self.original_color = 0
        self.new_color = 1

    def dig_lagoon(self):
        plan_pattern = re.compile(r"(\w) (\d+)")
        commands = []
        current_x, current_y = 0,0
        min_x, min_y, max_x, max_y = 0,0,0,0
        for line in self.dig_plan:
            match = plan_pattern.match(line)
            direction = match.group(1)
            distance = int(match.group(2))
            # color = match.group(3)
            if direction == "R":
                current_x += distance
            elif direction == "L":
                current_x -= distance
            elif direction == "U":
                current_y -= distance
            elif direction == "D":
                current_y += distance

            max_x = max(max_x, current_x)
            max_y = max(max_y, current_y)

            min_x = min(min_x, current_x)
            min_y = min(min_y, current_y)


            commands.append((direction, distance))

        self.site_width = max_x - min_x
        self.site_height = max_y - min_y
        offset_start = (abs(min_x), abs(min_y))
        self.dig(commands, offset_start)
        flood_start = (1,self.dig_site[0].index(1)+1)
        self.flood_fill(flood_start)

    def dig(self, commands, start):            
        self.dig_site = [[0 for _ in range(self.site_width+1)] for _ in range(self.site_height+1)]
        current_x , current_y = start
        self.dig_site[current_y][current_x] = 1
        for direction, distance in commands:
            if direction == "R":
                for _ in range(distance):
                    current_x += 1
                    self.dig_site[current_y][current_x] = self.new_color
            elif direction == "L":
                for _ in range(distance):
                    current_x -= 1
                    self.dig_site[current_y][current_x] = self.new_color
            elif direction == "U":
                for _ in range(distance):
                    current_y -= 1
                    self.dig_site[current_y][current_x] = self.new_color
            elif direction == "D":
                for _ in range(distance):
                    current_y += 1
                    self.dig_site[current_y][current_x] = self.new_color
    

    def flood_fill(self, start):
        stack = [start]

        while stack:
            x, y = stack.pop()
            if 0 <= x < self.site_height and 0 <= y < self.site_width and self.dig_site[x][y] == self.original_color:
                self.dig_site[x][y] = self.new_color

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))
    
        
    def print_plan(self):
        # Print the resulting grid
        for row in self.dig_site:
            for char in row:
                if char == 1:
                    print("#", end="")            
                else:
                    print(".", end="")
            print()

    def count_lava(self): 
        lava_count = 0
        for row in self.dig_site:
            lava_count += sum(row)
        return lava_count
            
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        lava_lagoon = LavaLagoon(puzzle_input)
        lava_lagoon.dig_lagoon()
        lava_count = lava_lagoon.count_lava()
        print(f"Solution to first problem: {lava_count}")
        # print(f"Solution to first problem: {lava_lagoon.calc_focusing_power()}")
        
