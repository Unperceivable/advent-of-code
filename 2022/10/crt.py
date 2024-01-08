# %%
import re
from pathlib import Path
from collections import namedtuple

class CRT():
    def __init__(self, puzzle_input: "list[str]"):
        self.cycle_monitor = [20,60,100,140,180,220]
        self.instructions = puzzle_input
        self.signal_strengths = []
        self.x = 1
        self.num_cycle = 0
    
    def execute_instructions(self):
        for instruction in self.instructions:
            commands = instruction.split(" ")
            if len(commands) == 2:
                for cycle in range(2):
                    self.num_cycle += 1
                    self.monitor_cycle()
                    if cycle:
                        self.x += int(commands[1])
            else:
                self.num_cycle += 1
                self.monitor_cycle()
        print()

    def monitor_cycle(self):
        self.print() 
        if self.num_cycle in self.cycle_monitor:
            self.signal_strengths.append(self.x)
        
        if self.num_cycle+20 in self.cycle_monitor:
            print()
        

    def print(self):
        within_sprite_l = self.x >= self.num_cycle%40-2
        within_sprite_r = self.x <= self.num_cycle%40
        char = "."
        if within_sprite_l and within_sprite_r:
            char = "#"
        print(char, end="")
        
    def sum_signal_strengths(self):
        return sum([s*c for s,c in zip(self.signal_strengths, self.cycle_monitor)])
    
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        crt = CRT(puzzle_input)
        crt.execute_instructions()
        sum_sig_strs = crt.sum_signal_strengths()
        print(f"Solutions to second problem displayed above")
        print(f"Solutions to first problem: {sum_sig_strs}")