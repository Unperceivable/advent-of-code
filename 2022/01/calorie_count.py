# %%
from pathlib import Path

class CalorieCount():
    
    def __init__(self, puzzle_input: "list[str]"):
        
        self.backpack = puzzle_input + [""]
        print(self.backpack)
        self.top_calories = self.get_top_3_calories()
        
    def most_calories(self): 
        return self.top_calories[0]

    def get_top_3_calories(self):
        top_calories = []
        current_elf_calories = 0
        for item in self.backpack:
            if item:
                current_elf_calories += int(item)
            else:
                print((top_calories, current_elf_calories))
                if top_calories:
                    for idx, calories in enumerate(top_calories):
                        if current_elf_calories > calories:
                            top_calories.insert(idx, current_elf_calories)
                            if len(top_calories) > 3:
                                top_calories.pop()
                            break
                else:
                    top_calories.append(current_elf_calories)
                current_elf_calories = 0
        return top_calories

    def sum_top_3_calories(self):
        return sum(self.top_calories)

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        calorie_count = CalorieCount(puzzle_input)
        print(f"Solutions to first problem: {calorie_count.most_calories()}")
        print(f"Solutions to second problem: {calorie_count.sum_top_3_calories()}")