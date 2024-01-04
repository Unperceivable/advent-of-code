# %%
import re
from pathlib import Path
from collections import defaultdict

class Tuning():
    
    def __init__(self, puzzle_input: "list[str]"):
        self.communication = puzzle_input
        
    def get_marker(self, msg_len=4):
        line_len = len(self.communication)
        for idx in range(msg_len,line_len,1):
            unique_chars = len(set(self.communication[idx-msg_len:idx]))
            if unique_chars == msg_len:
                return idx

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        tuning = Tuning(puzzle_input[0])
        print(f"Solutions to first problem: {tuning.get_marker(msg_len=4)}")
        print(f"Solutions to second problem: {tuning.get_marker(msg_len=14)}")