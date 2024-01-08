# %%
import re
from pathlib import Path
from collections import namedtuple

class CRT():
    def __init__(self, puzzle_input: "list[str]", cycle_monitor: "list[int]"):
        self.cycle_monitor = cycle_monitor
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

    def monitor_cycle(self):
        if self.num_cycle in self.cycle_monitor:
            self.signal_strengths.append(self.x)
    
    def sum_signal_strengths(self):
        return sum([s*c for s,c in zip(self.signal_strengths, self.cycle_monitor)])
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        crt = CRT(puzzle_input, cycle_monitor=[20,60,100,140,180,220])
        crt.execute_instructions()
        print(f"Solutions to first problem: {crt.sum_signal_strengths()}")