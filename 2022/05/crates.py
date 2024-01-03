# %%
import re
from pathlib import Path
from collections import defaultdict

class Crates():
    
    def __init__(self, puzzle_input: "list[str]"):
        self.instructions = None
        self.crates = self.get_crates(puzzle_input)
        
    def get_crates(self, input):
        crates = defaultdict(list)
        for idx, line in enumerate(input, start=1):
            if line and "1" not in line:
                values = line[1::4]
                for i, val in enumerate(values, start=1):
                    if val != " ":
                        crates[str(i)].append(val)
            else:
                self.instructions = input[idx+1:]
                break
        return crates
        
    def rearrange(self, save_order=False):
        instruction_pattern = re.compile("move (\d+) from (\d) to (\d)")
        for line in self.instructions:
            match = instruction_pattern.match(line)
            num, source, sink = int(match.group(1)), match.group(2), match.group(3)
            source_val = self.crates[source]
            sink_val = self.crates[sink]
            new_sink = source_val[:num]
            if not save_order:
                new_sink.reverse()
            new_sink = new_sink + sink_val
            new_source = source_val[num:]
            self.crates[source] = new_source
            self.crates[sink] = new_sink
        
    def top_crates(self):
        num_crates = len(list(self.crates.keys()))
        top_crates = "".join([self.crates[str(idx)][0] for idx in range(1,num_crates+1)]) 
        return top_crates
         
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        crates = Crates(puzzle_input)
        crates.rearrange()
        print(f"Solutions to first problem: {crates.top_crates()}")
        crates = Crates(puzzle_input)
        crates.rearrange(save_order=True)
        print(f"Solutions to second problem: {crates.top_crates()}")