# %%
from pathlib import Path

class Backpack():
    
    def __init__(self, puzzle_input: "list[str]"):
        
        self.backpacks = puzzle_input
        
    def sum_priorities(self): 
        sum_priorities = 0
        for backpack in self.backpacks:
            backpack_size = len(backpack)
            left = backpack[:backpack_size//2]
            right = backpack[backpack_size//2:]
            for char in left:
                if char in right:
                    sum_priorities += self.get_value(char)
                    break
                    
        return sum_priorities
    
    def badge_priorities(self):
        sum_priorities = 0
        num_backpacks = len(self.backpacks)
        for idx in range(0,num_backpacks,3):
            first = self.backpacks[idx]
            second = self.backpacks[idx+1]
            third =  self.backpacks[idx+2]
            for char in first:
                if char in second and char in third:
                    sum_priorities += self.get_value(char)
                    break

        return sum_priorities 

    def get_value(self,char):
        value = ord(char)
        if value > 97:
            value = value-96
        else:
            value = value-38
        return value
         
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        backpack = Backpack(puzzle_input)
        print(f"Solutions to first problem: {backpack.sum_priorities()}")
        print(f"Solutions to second problem: {backpack.badge_priorities()}")