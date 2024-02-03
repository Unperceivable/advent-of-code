from pathlib import Path
from collections import namedtuple
import numpy as np

Pos = namedtuple("Pos", ["x", "y"])

class SmokeBasin():
    def __init__(self, puzzle_input: "list[str]"):
        self.height_map = np.array([[int(i) for i in list(row)] for row in puzzle_input])

    def get_risk_level(self):
        up = Pos(0,-1)
        down = Pos(0,1)
        left = Pos(-1,0)
        right = Pos(1,0)
        moves = [up, down, left, right]
        
        map_height, map_width  = self.height_map.shape
        sum_risk_level = 0
        
        for y, row in enumerate(self.height_map):
            for x, point in enumerate(row):
                adj_points = []
                for move in moves:
                    pos = Pos(x+move.x, y+move.y)
                    within_width = ((0 <= pos.x) and (pos.x < map_width))
                    within_height = ((0 <= pos.y) and (pos.y < map_height))

                    if within_width and within_height:
                        adj_points.append(self.height_map[pos.y, pos.x])

                if all([point < adj_point for adj_point in adj_points]):
                    sum_risk_level += point + 1
        
        return sum_risk_level

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        smoke_basin = SmokeBasin(puzzle_input)
        print(f"Solution to first problem: {smoke_basin.get_risk_level()}")