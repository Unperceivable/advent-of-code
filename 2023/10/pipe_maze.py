
"""Solutions to https://adventofcode.com/2023/day/10 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path

Coord = namedtuple("Coord", ["x", "y"])

class PipeMaze():
    
    def __init__(self, maze: "list[str]"):
        self.maze = maze
        self.maze_width = len(self.maze[0])
        self.maze_height = len(self.maze)
        self.start_coord = self.get_start_coord()
        self.furthest_from_start = 0
        self.enclosed_tiles = 0
        self.map = [list(self.maze_width*".") for _ in range(self.maze_height)]
    
    def mark_on_map(self, coord, tile_marker=False):
        marker = self.furthest_from_start
        if tile_marker:
            marker = "I"
        self.map[coord.y][coord.x] = marker
    
    def marked_on_map(self, coord):
        return self.map[coord.y][coord.x] != "."
         
    def get_start_coord(self):
        for y, line in enumerate(self.maze):
            for x, char in enumerate(line):
                if char == "S":
                    return Coord(x, y)
        
    def get_next_valid_coords(self, coord, value):
        north = Coord(coord.x, coord.y - 1)
        south = Coord(coord.x, coord.y + 1)
        east = Coord(coord.x +1, coord.y)
        west = Coord(coord.x -1, coord.y)

        valid_coords = []
        
        if west.x >= 0 and value in ["S", "-", "J", "7"] and self.maze[west.y][west.x] in ["-", "L", "F"]:
            self.marked_on_map(west)
            valid_coords.append(west)
        
        if east.x < self.maze_width and value in ["S", "-", "L", "F"] and self.maze[east.y][east.x] in ["-", "7", "J"]:
            self.marked_on_map(east)
            valid_coords.append(east)
        
        if north.y >= 0 and value in ["S","|","L","J"] and self.maze[north.y][north.x] in ["|", "7","F"]:
            self.marked_on_map(north)
            valid_coords.append(north)
        
        if south.y < self.maze_height and value in ["S", "|", "7", "F"] and self.maze[south.y][south.x] in ["|", "L","J"]:
            self.marked_on_map(south)
            valid_coords.append(south)
            
        return valid_coords
    
    def print_map(self):
        for line in self.map:
            print("".join(map(str,line)))
           
    def max_dist_from_start(self):
        """Return maximum number of steps to the point farthest from the starting position."""
        current_coords = [self.start_coord]
        while current_coords:
            next_valid_coords = []
            for coord in current_coords:
                if not self.marked_on_map(coord):
                    self.mark_on_map(coord)
                    value = self.maze[coord.y][coord.x]
                    next_valid_coords.extend(self.get_next_valid_coords(coord,value))

            if next_valid_coords:
                current_coords = next_valid_coords
                self.furthest_from_start +=1
            else:
                current_coords = None

            # self.print_map()
        return self.furthest_from_start-1
    
    def num_enclosed_tiles(self):    
        vertical_enclosures = ["-", "L", "J", "7", "F", "S"]
        horizontal_enclosures = ["|", "L", "J", "7", "F", "S"]
        for y in range(self.maze_height):
            horizontal_toggle = False
            vertical_toggle = False
            for x, value in enumerate(self.maze[y]):
                coord = Coord(x,y)
                
                if value in horizontal_enclosures:
                    horizontal_toggle = not horizontal_toggle
                if value in vertical_enclosures:
                    vertical_toggle = not vertical_toggle
                
                if (horizontal_toggle and vertical_toggle) and value == ".":
                    self.enclosed_tiles +=1
                    self.mark_on_map(coord)
        self.print_map()
        return self.enclosed_tiles
    
    
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.readlines()
        print(f"Solution to first problem: {PipeMaze(puzzle_input).max_dist_from_start()}")
        print(f"Solution to second problem: {PipeMaze(puzzle_input).num_enclosed_tiles()}")