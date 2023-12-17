# %%
"""Solutions to https://adventofcode.com/2023/day/15 Puzzles."""
import re
from pathlib import Path
from collections import namedtuple
import hashlib

Pos = namedtuple("Pos", ["x", "y"])

class CruciblePath():
    def __init__(self, heatmap: "list[str]", start_pos=Pos(0,0)):
        self.heatloss = 0
        self.path = [start_pos]
        self.heatmap = heatmap
        self.heatmap_width = len(self.heatmap[0])
        self.heatmap_height = len(self.heatmap)
    
    def move_hor(self, vx):
        if vx:
            dx = vx//abs(vx)
            for _ in range(dx, vx+dx, dx):
                last_pos = self.last_pos()
                next_pos = Pos(last_pos.x+dx, last_pos.y)
                if self.inbound(next_pos):
                    self.path.append(next_pos)
                    self.heatloss += int(self.heatmap[next_pos.y][next_pos.x])

    def move_vert(self, vy):
        if vy:
            dy = vy//abs(vy)
            for _ in range(dy, vy+dy, dy):
                last_pos = self.last_pos()
                next_pos = Pos(last_pos.x, last_pos.y+dy)
                if self.inbound(next_pos):
                    self.path.append(next_pos)
                    self.heatloss += int(self.heatmap[next_pos.y][next_pos.x])

    def move(self, vector, run_first=True):

            vx = vector[0]
            vy = vector[1]
            
            if run_first:
                self.move_hor(vx)
                self.move_vert(vy)
            else:
                self.move_vert(vy)
                self.move_hor(vx)

    def inbound(self, pos):
        within_width = ((0 <= pos.x) and (pos.x <= self.heatmap_width-1))
        within_height = ((0 <= pos.y) and (pos.y <= self.heatmap_height-1))

        if within_width and within_height:
            return pos
        else:
            return None 

    def last_pos(self):
        return self.path[-1] 
    
    def valid_path(self, other):
        # print(self)
        goal_reached = (self.last_pos() == Pos(self.heatmap_width, self.heatmap_height))
        expected_len = (len(self.path) == 4)
        not_already_visited = True
        for pos in self.path:
            if pos in other:
                print((pos, other))
                not_already_visited = False
        is_valid = (expected_len or goal_reached) and not_already_visited
        # print(is_valid)
        return is_valid

    def __iadd__(self, other):
        if isinstance(other, CruciblePath):
            self.heatloss += other.heatloss
            self.path.extend(other.path)
        else:
            raise TypeError("Unsupported operand type. Must be CruciblePath.")
        return self
    
    def __str__(self):
        return f"{self.heatloss}, {self.path}"
    
    def print(self):
        for row in self.heatmap:
            print(row)
        print("---------")
        from copy import copy
        path = copy(self.path)
        for y in range(self.heatmap_height):
            for x in range(self.heatmap_width):
                char = "O"
                for pos in self.path:
                    if pos.x == x and pos.y == y:
                        char = "X"
                
                print(char, end="")
            print("")
        print("________")
        

class Crucible():
    
    def __init__(self, heatmap: "list[str]"):
        self.heatmap = heatmap
        self.path = CruciblePath(heatmap, Pos(0,0))
        print(self.path)
        self.heatmap_width = len(self.heatmap[0])
        self.heatmap_height = len(self.heatmap)
    

    def best_move(self):
        # print(self.path)
        last_pos = self.path.last_pos()
        potential_paths = [] 
        for vector, run_first in self.three_path_moves():
            # print(vector)
            next_path = CruciblePath(self.heatmap, last_pos)
            next_path.move(vector, run_first=run_first)
            if next_path.valid_path(self.path.path[1:]):
                next_path.path.pop(0)
                potential_paths.append(next_path)
        
        # print(potential_paths)
        if potential_paths:
            potential_paths = min(potential_paths, key=lambda x: x.heatloss) 
        return potential_paths
 
    def three_path_moves(self):
        moves = []
        for rise_first in [True, False]:
            for x in range(-3, 4):
                for y in range(-3, 4):
                    if abs(x) + abs(y) == 3:
                        moves.append(((x, y), rise_first))
            
        return moves

    def best_path(self):
        
        while self.path.last_pos() != Pos(self.heatmap_width, self.heatmap_height):
            self.path.print()
            best_move = self.best_move()
            if best_move:
                self.path += best_move
        

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        crucible = Crucible(puzzle_input)
        crucible.best_path()
        print(f"Solution to first problem: {crucible.heatloss}")
        # print(f"Solution to first problem: {crucible.calc_focusing_power()}")
        
