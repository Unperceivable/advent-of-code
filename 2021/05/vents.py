from pathlib import Path
from collections import namedtuple

import numpy as np

Line = namedtuple("Line", ["start", "end"])
Coord = namedtuple("Coord", ["x", "y"])

class Vents():
    def __init__(self, puzzle_input: "list[str]"):
        self.vent_lines = self.get_vent_lines(puzzle_input)

    def get_vent_lines(self, puzzle_input):
        self.max_x, self.max_y = 0,0
        lines = []
        for line in puzzle_input:
            start, end = [v.split(",") for v in line.split(" -> ")]
            sx,sy = [int(i) for i in start]
            ex,ey = [int(i) for i in end]
            self.max_x = max([self.max_x, sx, ex])
            self.max_y = max([self.max_y, sy, ey])
            lines.append(Line(Coord(sx,sy),Coord(ex,ey)))
        return lines

            

    def num_overlapping_lines(self, diagonal_lines=False):
        
        sea_floor = np.zeros(shape=(self.max_x+1, self.max_y+1))        
        for vent_line in self.vent_lines:
            diff_x = int(vent_line.end.x - vent_line.start.x)
            diff_y = int(vent_line.end.y - vent_line.start.y)

            if bool(diff_x) ^ bool(diff_y):
                if diff_x:
                    x_values =[vent_line.start.x, vent_line.end.x]
                    for x in range(min(x_values), max(x_values)+1):
                        sea_floor[vent_line.start.y, x] += 1
                if diff_y:
                    y_values = [vent_line.start.y, vent_line.end.y]
                    for y in range(min(y_values), max(y_values)+1):
                        sea_floor[y, vent_line.start.x] += 1
                
            elif diagonal_lines:
                step_x = int(diff_x/abs(diff_x))
                step_y = int(diff_y/abs(diff_y))
            
                x_values = range(vent_line.start.x, vent_line.end.x + step_x, step_x)
                y_values = range(vent_line.start.y, vent_line.end.y + step_y, step_y)

                print(vent_line)
                for x,y in zip(x_values, y_values):
                    print((x,y))
                    sea_floor[y, x] += 1

        print(sea_floor)
        print("-----------------")
        return np.sum(sea_floor > 1)

if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        vents = Vents(puzzle_input)
        print(f"Solution to first problem: {vents.num_overlapping_lines()}")
        print(f"Solution to second problem: {vents.num_overlapping_lines(diagonal_lines=True)}")