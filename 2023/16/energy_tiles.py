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
    
    def print(self):
        for tile_row, energy_row in zip(self.contraption, self.energized_tiles):
            for tile, energy in zip(tile_row, energy_row):
                if energy == 1:
                    print("o", end="")            
                else:
                    print(tile, end="")
            print()

    def energize_tiles(self):
        change_in_tiles = 0
        beams = [Beam(0,0,self.vel_right)]
        while beams and change_in_tiles < 20:
            new_beams = []
            energized_count_before = self.count_energized()
            for beam in beams:
                self.energized_tiles[beam.y][beam.x] = 1
                updated_beams = self.update_vel(beam) 
                new_beams.extend([self.update_pos(beam) for beam in updated_beams])
            energized_count_after = self.count_energized()
            if energized_count_after <= energized_count_before:
                change_in_tiles += 1
            beams = [beam for beam in new_beams if beam]
            if change_in_tiles > 0:
                print((energized_count_before, energized_count_after,len(beams)))
                for beam in beams:
                    print(beam)
        
    def count_energized(self):
        energized_tiles = 0
        for row in self.energized_tiles:
            energized_tiles += sum(row)
        return energized_tiles        

    def update_vel (self, beam):

        beams = []
        new_tile = self.contraption[beam.y][beam.x]
        from_left = beam.vel.x == 1
        from_right = beam.vel.x == -1
        from_up = beam.vel.y == 1
        from_down = beam.vel.y == -1
        
        if new_tile == "|":
            if from_left or from_right:
                beam_a = Beam(beam.x, beam.y, self.vel_up)
                beam_b = Beam(beam.x, beam.y, self.vel_down)
                beams.extend([beam_a, beam_b])
            else:
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
        


# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        energy_tiles = EnergyTiles(puzzle_input)
        energy_tiles.energize_tiles()
        print(f"Solution to first problem: {energy_tiles.count_energized()}")
        # print(f"Solution to first problem: {energy_tiles.calc_focusing_power()}")
        


