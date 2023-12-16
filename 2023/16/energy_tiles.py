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
        self.energized_tiles = [[0 for _ in range(self.contraption_width)] for _ in range(self.contraption_height)]

        self.vel_right = Vel(1, 0)
        self.vel_left = Vel(-1, 0)
        self.vel_up = Vel(0, -1)
        self.vel_down = Vel(0, 1)
    
    def print(self, thing: "list[str]"):
        for line in thing:
            print(line)

    def energize_tiles(self):
        change_in_tiles = True
        beams = [Beam(0,0,self.vel_right)]
        while beams and change_in_tiles < 100:
            new_beams = []
            for beam in beams:
                change_in_tiles += self.update_tiles(beam)
                updated_beams = self.update_vel(beam) 
                new_beams.extend([self.update_pos(beam) for beam in updated_beams])
            beams = [beam for beam in new_beams if beam]

        self.print(self.contraption)
        self.print(self.energized_tiles)
                
 
    def update_tiles(self, beam):
        energized_count_before = self.count_energized()
        self.energized_tiles[beam.y][beam.x] = 1
        energized_count_after = self.count_energized()
        return energized_count_after >= energized_count_before
        
    def get_hash(self, panel):
        hash_object = hashlib.sha256(''.join(panel).encode())
        hash_value = hash_object.hexdigest()[:8]
        return hash_value
            
    def count_energized(self):
        energized_tiles = 0
        for row in self.energized_tiles:
            energized_tiles += sum(row)
        return energized_tiles        

    def update_vel (self, beam):

        beams = []
        new_tile = self.contraption[beam.y][beam.x]
        print(new_tile)
        print(beam)
        from_left = beam.vel.x == 1
        from_right = beam.vel.x == -1
        from_up = beam.vel.y == 1
        from_down = beam.vel.y == -1
        
        print(from_left, from_right, from_up, from_down)
        
        if new_tile == "|":
            if from_left or from_right:
                beam_a = Beam(beam.x, beam.y, self.vel_up)
                beam_b = Beam(beam.x, beam.y, self.vel_down)
                beams.extend([beam_a, beam_b])
            else:
                print("WHY ARE YOU HERHERHERE!>>!>")
                beams.append(beam)
        elif new_tile == "-":
            if from_up or from_down:
                beam_a = Beam(beam.x, beam.y, self.vel_left)
                beam_b = Beam(beam.x, beam.y, self.vel_right)
                beams.extend([beam_a, beam_b])
            else:
                beams.append(beam)
        
        elif new_tile == "\\":
            if from_left:
                beam.vel = self.vel_down
            elif from_right:
                beam.vel = self.vel_up
            elif from_up:
                beam.vel = self.vel_right
            elif from_down:
                beam.vel = self.vel_left
            beams.append(beam)
                
        elif new_tile == "/":
            if from_left:
                beam.vel = self.vel_up
            elif from_right:
                beam.vel = self.vel_down
            elif from_up:
                beam.vel = self.vel_left
            elif from_down:
                beam.vel = self.vel_right
            beams.append(beam)
        else:
            beams.append(beam)
        
        print("__________")
        for beam in beams:
            print(beam)
        print("__________")
        
        return beams 

    def update_pos(self, beam):
        print(beam)
        beam.x = beam.x + beam.vel.x
        within_width = ((0 <= beam.x) and (beam.x <= self.contraption_width-1))
        
        beam.y = beam.y + beam.vel.y
        within_height = ((0 <= beam.y) and (beam.y <= self.contraption_height-1))

        if within_width and within_height:
            return beam
        else:
            return None 
        

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        energy_tiles = EnergyTiles(puzzle_input)
        energy_tiles.energize_tiles()
        print(f"Solution to first problem: {energy_tiles.count_energized()}")
        # print(f"Solution to first problem: {energy_tiles.calc_focusing_power()}")
        
