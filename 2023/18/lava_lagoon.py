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

    def get_dist_and_direction(self, line, hex=False):
        if hex:
            hex_map = {0:"R", 1: "D", 2:"L", 3:"U"}
            plan_pattern = re.compile(r"\w \d+ \(#(\w+)\)")
            match = plan_pattern.match(line)
            hex_value = match.group(1)
            distance = int(hex_value[:-1], 16)
            direction = hex_map[int(hex_value[-1], 16)]
            return distance, direction
        else:
            plan_pattern = re.compile(r"(\w) (\d+)")
            match = plan_pattern.match(line)
            direction = match.group(1)
            distance = int(match.group(2))
            return distance, direction
        
    def dig_lagoon(self, hex=False):
        current_x, current_y = 0,0
        points = [(current_x, current_y)]
        perimeter = 0
        for line in self.dig_plan:
            distance, direction = self.get_dist_and_direction(line, hex=hex)
            if direction == "R":
                current_x += distance
            elif direction == "L":
                current_x -= distance
            elif direction == "U":
                current_y -= distance
            elif direction == "D":
                current_y += distance
            perimeter += distance
            points.append((current_x, current_y))

        area = int(self.polygon_area(points))
        return area+(perimeter//2)+1

    def polygon_area(self, points):
        n = len(points)
        if n < 3:
            raise ValueError("A polygon must have at least 3 points.")

        # Apply the Shoelace formula
        area = 0.0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]  # Use modulo to wrap around to the first point
            area += (x1 * y2 - x2 * y1)

        area = abs(area) / 2.0
        return area

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
        lava_count = lava_lagoon.dig_lagoon()
        print(f"Solution to first problem: {lava_count}")
        lava_count = lava_lagoon.dig_lagoon(hex=True)
        print(f"Solution to first problem: {lava_count}")
        # print(f"Solution to first problem: {lava_lagoon.calc_focusing_power()}")
        
