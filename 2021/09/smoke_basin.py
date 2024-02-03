from pathlib import Path
from collections import namedtuple
import numpy as np

Pos = namedtuple("Pos", ["x", "y"])

class SmokeBasin():
    def __init__(self, puzzle_input: "list[str]"):
        self.height_map = np.array([[int(i) for i in list(row)] for row in puzzle_input])
        self.map_height, self.map_width  = self.height_map.shape

    def get_risk_level(self):
        lowest_points = self.get_lowest_points()
        sum_risk_level = sum([self.height_map[pos.y, pos.x] + 1 for pos in lowest_points])
        return sum_risk_level
    
    def get_lowest_points(self):
        up = Pos(0,-1)
        down = Pos(0,1)
        left = Pos(-1,0)
        right = Pos(1,0)
        moves = [up, down, left, right]
        
        lowest_points = []
        for y, row in enumerate(self.height_map):
            for x, point in enumerate(row):
                adj_points = []
                for move in moves:
                    pos = Pos(x+move.x, y+move.y)
                    within_width = ((0 <= pos.x) and (pos.x < self.map_width))
                    within_height = ((0 <= pos.y) and (pos.y < self.map_height))

                    if within_width and within_height:
                        adj_points.append(self.height_map[pos.y, pos.x])

                if all([point < adj_point for adj_point in adj_points]):
                    lowest_points.append(Pos(x,y))
        
        return lowest_points
    
    def prod_largest_basins(self):
        basin_sizes = []
        lowest_points = self.get_lowest_points()
        for point in lowest_points:
            basin_sizes.append(self.get_basin_size(point, 9))
        basin_sizes = sorted(basin_sizes, reverse=True)
        top_3 = np.array(basin_sizes[:3])
        return np.prod(top_3)

    def get_basin_size(self, start, boarder):
        basin_size = 0
        stack = [start]
        while stack:
            pos = stack.pop()
            within_width = ((0 <= pos.x) and (pos.x < self.map_width))
            within_height = ((0 <= pos.y) and (pos.y < self.map_height))
            if  within_height and within_width:
                not_boarder = self.height_map[pos.y, pos.x] != boarder
                if not_boarder:
                    self.height_map[pos.y, pos.x] = boarder
                    basin_size += 1

                    stack.append(Pos(pos.x + 1, pos.y))
                    stack.append(Pos(pos.x - 1, pos.y))
                    stack.append(Pos(pos.x, pos.y + 1))
                    stack.append(Pos(pos.x, pos.y - 1))

        return basin_size

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        smoke_basin = SmokeBasin(puzzle_input)
        print(f"Solution to first problem: {smoke_basin.get_risk_level()}")
        print(f"Solution to second problem: {smoke_basin.prod_largest_basins()}")