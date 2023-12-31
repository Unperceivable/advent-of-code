# %%
from pathlib import Path

class RockPaperScissors():
    
    def __init__(self, puzzle_input: "list[str]"):
        
        self.strategy = puzzle_input
        self.strat_a = {"A X": 4,
                        "A Y": 8,
                        "A Z": 3,
                        "B X": 1,
                        "B Y": 5,
                        "B Z": 9,
                        "C X": 7,
                        "C Y": 2,
                        "C Z": 6}
        
        self.strat_b = {"A X": 3,
                        "A Y": 4,
                        "A Z": 8,
                        "B X": 1,
                        "B Y": 5,
                        "B Z": 9,
                        "C X": 2,
                        "C Y": 6,
                        "C Z": 7}
        
    def play(self, strat="a"): 
        total_score = 0
        if strat == "a":
            strat = self.strat_a
        else:
            strat = self.strat_b

        for line in self.strategy:
            total_score += strat[line]
        return total_score
        
            

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        rock_paper_scissors = RockPaperScissors(puzzle_input)
        print(f"Solutions to first problem: {rock_paper_scissors.play(strat='a')}")
        print(f"Solutions to second problem: {rock_paper_scissors.play(strat='b')}")