# %%
from pathlib import Path
from collections import namedtuple
import numpy as np

Coord = namedtuple("Coord", ["x", "y", "z"])

class Boulder():
    def __init__(self, puzzle_input: "list[str]", num_rocks=2022):
        self.max_x, self.max_y, self.max_z = 0,0,0
        self.voxels = []
        for line in puzzle_input:
            voxel = [int(val) for val in eval(line)]
            voxel = Coord(*voxel)
            self.max_x = max(self.max_x, voxel.x+2)
            self.max_y = max(self.max_y, voxel.y+2)
            self.max_z = max(self.max_z, voxel.z+2)
            self.voxels.append(voxel)

    
    def get_lava_drop_surface(self):
        surface_area = 0
        lava_drop = np.zeros((self.max_x, self.max_y, self.max_z))
        for voxel in self.voxels:
            lava_drop[voxel.x, voxel.y, voxel.z] = 1

        up = Coord(0,0,-1)
        down = Coord(0,0,-1)
        left = Coord(-1,0,0)
        right = Coord(1,0,0)
        forward = Coord(0,1,0)
        backward = Coord(0,-1,0)

        moves = [forward, backward, up, down, left, right]
        for voxel in self.voxels:
            for move in moves: 
                x = voxel.x + move.x
                y = voxel.y + move.y
                z = voxel.z + move.z
                if lava_drop[x,y,z] == 0:
                    surface_area += 1
        return surface_area
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        boulder = Boulder(puzzle_input)
        print(f"Solution to first problem: {boulder.get_lava_drop_surface()}")