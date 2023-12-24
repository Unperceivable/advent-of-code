# %%
from pathlib import Path
from collections import namedtuple
import sys

sys.setrecursionlimit(100000)

Coord = namedtuple("Coord", ["x", "y"])
from copy import copy

class Vector():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

class Hail():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        
    def __str__(self):
        return f"{self.pos} : {self.vel}"

class HailStorm():
    
    def __init__(self, puzzle_input: "list[str]", min_pos, max_pos):
        
        self.hail = []
        self.min_pos, self.max_pos = min_pos, max_pos
        for hail in puzzle_input:
            hail_pos, hail_vel = hail.split("@")
            hail_pos = [int(val) for val in hail_pos.split(",")]
            hail_vel = [int(val) for val in hail_vel.split(",")]
            hail = Hail(Vector(*hail_pos), Vector(*hail_vel))
            self.hail.append(hail)

        
        
    def get_2d_collisions(self):
        """Calculate the number of collisions between"""
        collisions = []
        num_hail = len(self.hail)
        for a in range(num_hail):
            for b in range(a+1, num_hail):
                if a != b:
                    hail_a = self.hail[a]
                    hail_b = self.hail[b]

                    collision = self.intersection_point(hail_a, hail_b)
                    if collision and self.within_boundary(collision):
                        collisions.append(collision)

        print(collisions)
        return len(collisions)

    def within_boundary(self, pos):
        x,y = pos
        within_x = self.min_pos <= x  and x <= self.max_pos
        within_y = self.min_pos <= y  and y <= self.max_pos
        return within_x and within_y

    def intersection_point(self, v1,v2):
        """Calculate the intersection point of two 2d line segments given their endpoints."""
        x1, y1 = v1.pos.x, v1.pos.y
        vx1, vy1 = v1.vel.x, v1.vel.y
        x2, y2 = v2.pos.x, v2.pos.y
        vx2, vy2 = v2.vel.x, v2.vel.y

        # Check if the objects are already on the same line
        if vx1 * vy2 == vx2 * vy1:
            return None

        # Calculate the time of collision using the slope-intercept method
        t = ((x1 - x2) * vy2 - (y1 - y2) * vx2) / (vx1 * vy2 - vx2 * vy1)

        # Calculate the collision point
        collision_x = x1 + t * vx1
        collision_y = y1 + t * vy1
        return collision_x, collision_y


# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        # hail_storm = HailStorm(puzzle_input)
        # print(f"Solutions to first problem: {hail_storm.get_collisions(slippery=True)}")
        hail_storm = HailStorm(puzzle_input)
        print(f"Solution to second problem: {hail_storm.get_collisions(slippery=False)}")