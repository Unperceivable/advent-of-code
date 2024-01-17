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

    
    def get_lava_drop_surface(self, exclude_pockets=False):
        self.lava_drop = np.zeros((self.max_x, self.max_y, self.max_z))
        for voxel in self.voxels:
            self.lava_drop[voxel.x, voxel.y, voxel.z] = 1
        
        surface_area = self.check_sides(self.voxels, side_value=0)
        
        if exclude_pockets:
            self.flood_fill(0,1)
            air_pockets = np.column_stack(np.where(self.lava_drop == 0))
            air_pockets = [Coord(*pocket) for pocket in air_pockets]
            pocket_area = self.check_sides(air_pockets, side_value=1) 
            surface_area -= pocket_area
        
        return surface_area

    def check_sides(self, voxels, side_value):
        surface_area = 0
        up = Coord(0,0,-1)
        down = Coord(0,0,-1)
        left = Coord(-1,0,0)
        right = Coord(1,0,0)
        forward = Coord(0,1,0)
        backward = Coord(0,-1,0)

        moves = [forward, backward, up, down, left, right]
        for voxel in voxels:
            for move in moves: 
                x = voxel.x + move.x
                y = voxel.y + move.y
                z = voxel.z + move.z
                if self.lava_drop[x,y,z] == side_value:
                    surface_area += 1
        return surface_area

    def flood_fill(self, target_value, replacement_value):
        x, y, z = (0, 0, 0)
        if self.lava_drop[x, y, z] != target_value:
            return

        stack = [(x, y, z)]
        while stack:
            current_x, current_y, current_z = stack.pop()
            self.lava_drop[current_x, current_y, current_z] = replacement_value

            neighbors = [
                (current_x + 1, current_y, current_z),
                (current_x - 1, current_y, current_z),
                (current_x, current_y + 1, current_z),
                (current_x, current_y - 1, current_z),
                (current_x, current_y, current_z + 1),
                (current_x, current_y, current_z - 1)
            ]

            for neighbor_x, neighbor_y, neighbor_z in neighbors:
                if (
                    0 <= neighbor_x < self.lava_drop.shape[0] and
                    0 <= neighbor_y < self.lava_drop.shape[1] and
                    0 <= neighbor_z < self.lava_drop.shape[2] and
                    self.lava_drop[neighbor_x, neighbor_y, neighbor_z] == target_value
                ):
                    stack.append((neighbor_x, neighbor_y, neighbor_z))


# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        boulder = Boulder(puzzle_input)
        print(f"Solution to first problem: {boulder.get_lava_drop_surface()}")
        boulder = Boulder(puzzle_input)
        print(f"Solution to first problem: {boulder.get_lava_drop_surface(exclude_pockets=True)}")