"""Solutions to https://adventofcode.com/2023/day/11 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path
from itertools import combinations

Coord = namedtuple("Coord", ["x", "y"])

class Observatory():
    
    def __init__(self, image: "list[str]", expansion_factor=2):
        self.image = image
        # assumed image width and hieght is the same
        self.image_width = len(self.image[0])
        self.image_height = self.image_width
        
        self.expansion_factor = expansion_factor

        self.expand_empty_space()
        self.galaxy_coords = self.get_galaxy_coords()
    
    def is_empty_space(self, space):
        if "#" in space:
            return False
        else:
            return True

    def get_galaxy_dist(self, first_galaxy, second_galaxy):
        base_distance = abs(second_galaxy.x - first_galaxy.x) + abs(second_galaxy.y - first_galaxy.y)
        expansion_adjustment = 0
        
        x_min = min(first_galaxy.x, second_galaxy.x)
        x_max = max(first_galaxy.x, second_galaxy.x)
        expanded_cols_between_galaxies = len([col for col in self.expanded_cols if x_min < col and col < x_max])
        if expanded_cols_between_galaxies:
            expansion_adjustment += expanded_cols_between_galaxies*self.expansion_factor - expanded_cols_between_galaxies
        
        y_min = min(first_galaxy.y, second_galaxy.y)
        y_max = max(first_galaxy.y, second_galaxy.y)
        expanded_rows_between_galaxies = len([row for row in self.expanded_rows if y_min < row and row < y_max])
        if expanded_rows_between_galaxies:
            expansion_adjustment += expanded_rows_between_galaxies*self.expansion_factor - expanded_rows_between_galaxies
        
        return base_distance + expansion_adjustment
    
    def expand_empty_space(self):
        self.expanded_rows = []
        self.expanded_cols = []
        for idx in range(self.image_width):
            row = self.image[idx] 
            if self.is_empty_space(row):
                self.expanded_rows.append(idx)
            
            column = "".join(map(str, [self.image[row][idx] for row in range(self.image_height)]))
            if self.is_empty_space(column):
                self.expanded_cols.append(idx)
        
    def print_image(self):
        for line in self.image:
            print(line)
    
    def get_galaxy_coords(self):
        coords = []
        for y, line in enumerate(self.image):
            coords.extend([Coord(x,y) for x, char in enumerate(line) if char =="#"])
        return coords

    def sum_of_galaxy_dists(self):
        galaxy_distances = []
        
        galaxy_pairs = list(combinations(self.galaxy_coords, 2))
        for gal1, gal2 in galaxy_pairs:
            galaxy_distance = self.get_galaxy_dist(gal1, gal2)
            galaxy_distances.append(galaxy_distance)
        
        return sum(galaxy_distances)
    
    
    
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        print(f"Solution to first problem: {Observatory(puzzle_input, expansion_factor=2).sum_of_galaxy_dists()}")
        print(f"Solution to second problem: {Observatory(puzzle_input, expansion_factor=1000000).sum_of_galaxy_dists()}")