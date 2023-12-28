# %%
"""Solutions to https://adventofcode.com/2023/day/15 Puzzles."""
import re
from pathlib import Path
from collections import namedtuple
import hashlib

class Vel():
    def __init__(self, x, y):
        self.x = x
        self.y = y

Vel.right = Vel(1, 0)
Vel.left = Vel(-1, 0)
Vel.up = Vel(0, -1)
Vel.down = Vel(0, 1)

class Beam():
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.vel.x}, {self.vel.y})"

class EnergyTiles():
    
    def __init__(self, contraption: "list[str]"):
        self.contraption = contraption
        self.contraption_width = len(self.contraption[0])
        self.contraption_height = len(self.contraption)
    
    def print(self, energized_tiles):
        for tile_row, energy_row in zip(self.contraption, energized_tiles):
            for tile, energy in zip(tile_row, energy_row):
                if energy == 1:
                    print("o", end="")            
                else:
                    print(tile, end="")
            print()

    def energize_tiles(self, start=Beam(0,0,Vel.right)):
        energized_tiles = [[0 for _ in range(self.contraption_width)] for _ in range(self.contraption_height)]
        change_in_tiles = 0
        beams = [start]
        while beams and change_in_tiles < 20:
            new_beams = []
            energized_count_before = self.count_energized(energized_tiles)
            for beam in beams:
                energized_tiles[beam.y][beam.x] = 1
                _new_beams = [self.update_pos(new_beam) for new_beam in self.update_vel(beam)]
                new_beams.extend(_new_beams) 
            beams = [beam for beam in new_beams if beam]    
            energized_count_after = self.count_energized(energized_tiles)
            if energized_count_after <= energized_count_before:
                change_in_tiles += 1

        return energized_count_after
    
    def count_energized(self, energized_tiles):
        num_energized = 0
        for row in energized_tiles:
            num_energized += sum(row)
        return num_energized        

    def update_vel (self, beam):

        beams = []
        new_tile = self.contraption[beam.y][beam.x]
        from_left = beam.vel.x == 1
        from_right = beam.vel.x == -1
        from_up = beam.vel.y == 1
        from_down = beam.vel.y == -1
        
        if new_tile == "|":
            if from_left or from_right:
                beam_a = Beam(beam.x, beam.y, Vel.up)
                beam_b = Beam(beam.x, beam.y, Vel.down)
                beams.extend([beam_a, beam_b])
            else:
                beams.append(beam)
        elif new_tile == "-":
            if from_up or from_down:
                beam_a = Beam(beam.x, beam.y, Vel.left)
                beam_b = Beam(beam.x, beam.y, Vel.right)
                beams.extend([beam_a, beam_b])
            else:
                beams.append(beam)
        
        elif new_tile == "\\":
            if from_left:
                beam.vel = Vel.down
            elif from_right:
                beam.vel = Vel.up
            elif from_up:
                beam.vel = Vel.right
            elif from_down:
                beam.vel = Vel.left
            beams.append(beam)
                
        elif new_tile == "/":
            if from_left:
                beam.vel = Vel.up
            elif from_right:
                beam.vel = Vel.down
            elif from_up:
                beam.vel = Vel.left
            elif from_down:
                beam.vel = Vel.right
            beams.append(beam)
        else:
            beams.append(beam)
        
        return beams 

    def update_pos(self, beam):
        beam.x = beam.x + beam.vel.x
        within_width = ((beam.x >= 0 ) and (beam.x <= self.contraption_width-1))
        
        beam.y = beam.y + beam.vel.y
        within_height = ((beam.y >=0) and (beam.y <= self.contraption_height-1))

        if within_width and within_height:
            return beam
        else:
            return None 
        
    def max_energizeable(self):
        max_energized = 0

        # Right edge
        for i in range(self.contraption_height):
            start = Beam(self.contraption_width-1, i, Vel.left)
            print(f"{i}, {start}, {max_energized}")
            max_energized = max(max_energized, self.energize_tiles(start))
        
        # Top edge
        for i in range(self.contraption_width):
            start = Beam(i, 0, Vel.down)
            print(f"{i}, {start}, {max_energized}")
            max_energized = max(max_energized, self.energize_tiles(start))

        # Bottom edge
        for i in range(self.contraption_width):
            start = Beam(i, self.contraption_height-1, Vel.up)
            print(f"{i}, {start}, {max_energized}")
            max_energized = max(max_energized, self.energize_tiles(start))

        # Left edge
        for i in range(self.contraption_height):
            start = Beam(0,i,Vel.right)
            print(f"{i}, {start}, {max_energized}")
            max_energized = max(max_energized, self.energize_tiles(start))
           
        return max_energized

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        energy_tiles = EnergyTiles(puzzle_input)
        # print(f"Solution to first problem: {energy_tiles.energize_tiles()}")
        print(f"Solution to second problem: {energy_tiles.max_energizeable()}")
        


