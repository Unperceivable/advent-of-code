# %%
import re
from pathlib import Path
from collections import defaultdict

class Device():
    
    def __init__(self, puzzle_input: "list[str]"):
        self.dir_sizes = self.get_dir_structure(puzzle_input)
        self.total_space = 70000000
        self.required_space = 30000000
    
    def get_dir_structure(self, cli_logs):
        dir_sizes = defaultdict(int)
        size_pattern = re.compile("\d+")
        current_dir = []
        for line in cli_logs:
            command = line.split()
            if len(command) == 3:
                if ".." == command[2]:
                    current_dir = current_dir[:-1]
                else:
                    current_dir.append(command[2])
            else:
                match = size_pattern.search(command[0])
                if match:
                    size = int(match.group(0))
                    dir = Path()
                    for _dir in current_dir:
                        dir = dir.joinpath(_dir)
                        dir_sizes[str(dir)] += size
        return dir_sizes
    
    def sum_dir_sizes(self, size_limit=100000):
        sum_dir_sizes = 0
        for dir, size in self.dir_sizes.items():
            if size <= size_limit:
                sum_dir_sizes += size
        return sum_dir_sizes

    def min_dir_size_for_deletion(self):
        min_dir_size_for_deletion = self.total_space
        free_space = self.total_space - self.dir_sizes["/"]
        free_space_required = self.required_space - free_space
        for size in self.dir_sizes.values():
            if size >= free_space_required and size < min_dir_size_for_deletion:
                min_dir_size_for_deletion = size
        return min_dir_size_for_deletion
        
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        device = Device(puzzle_input)
        print(f"Solutions to first problem: {device.sum_dir_sizes()}")
        print(f"Solutions to second problem: {device.min_dir_size_for_deletion()}")