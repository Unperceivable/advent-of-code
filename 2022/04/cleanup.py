# %%
from pathlib import Path

class Cleanup():
    
    def __init__(self, puzzle_input: "list[str]"):
        self.pairs = puzzle_input
        
        
        
    def sum_full_subranges(self): 
        sum_pairs = 0
        for  line in self.pairs:
            first_range, second_range = line.split(",")
            first_range = [int(bound) for bound in first_range.split("-")]
            second_range = [int(bound) for bound in second_range.split("-")]
            sum_pairs += all(self.bound_check(first_range, second_range)) or all(self.bound_check(second_range, first_range))
        return sum_pairs
    
    def bound_check(self, values: "list[int]", bounds: "list[int]"):
            return  [val >= bounds[0] and val <= bounds[1] for val in values]
    
    def sum_partial_subranges(self): 
        sum_pairs = 0
        for  line in self.pairs:
            first_range, second_range = line.split(",")
            first_range = [int(bound) for bound in first_range.split("-")]
            second_range = [int(bound) for bound in second_range.split("-")]
            sum_pairs += any(self.bound_check(first_range, second_range)) or any(self.bound_check(second_range, first_range))
        return sum_pairs
         
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        cleanup = Cleanup(puzzle_input)
        print(f"Solutions to first problem: {cleanup.sum_full_subranges()}")
        print(f"Solutions to second problem: {cleanup.sum_partial_subranges()}")