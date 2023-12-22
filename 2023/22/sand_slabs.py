# %%
from pathlib import Path
from collections import namedtuple, defaultdict
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
    
class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

class Brick:
    def __init__(self, bottom_left: Coord, top_right: Coord):
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.length = top_right.z - bottom_left.z +1
    def __str__(self):
        return f"{self.bottom_left}, {self.top_right}, {self.length}"

class SandSlabs():
    def __init__(self, puzzle_input: "list[str]"):
        self.brick_list = puzzle_input
        self.max_x, self.max_y, self.max_z = 0,0,0 
        self.bricks = self.get_bricks()
        array_size = self.max_x, self.max_y, self.max_z
        self.array = self.create_3d_array(array_size)
        self.visualize_3d_array()
        self.print_bricks()

    def print_bricks(self):
        for brick in self.bricks:
            print(brick)
    
    def get_bricks(self): 
        bricks = []
        for line in self.brick_list:
            brick_start, brick_end = line.split("~")
            brick_start = [int(val) for val in brick_start.split(",")]
            brick_end = [int(val) for val in brick_end.split(",")]
            brick = Brick(Coord(*brick_start), Coord(*brick_end))
            self.max_x = max(self.max_x, brick.bottom_left.x)
            self.max_y = max(self.max_y, brick.top_right.y)
            self.max_z += brick.length
            bricks.append(brick)
        bricks = sorted(bricks, key=lambda brick: brick.bottom_left.z)
        return bricks

    def create_3d_array(self, array_size):
        return np.zeros(array_size)

    def place_brick(self, brick):
        
        contact_height = 0
        for y in brick.bottom_left:
            
        
    def visualize_3d_array(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x, y, z = np.where(self.array == 1)
        ax.scatter(x, y, z, c='b', marker='s')

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.set_title('3D Array Visualization')

        plt.show()

                
                    
        
    
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        sand_slabs = SandSlabs(puzzle_input)
        # num_plots = sand_slabs.reachable_plots(steps=64)
        # print(f"Solution to first problem: {num_plots}")
        # print(f"Solution to second problem: {sand_slabs.distinct_ratings()}")
        