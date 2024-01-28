from pathlib import Path
from collections import defaultdict
import numpy as np
class SquidBingo():
    def __init__(self, puzzle_input: "list[str]"):
        self.numbers = [int(v) for v in puzzle_input[0].split(",")]
        self.boards = self.get_boards(puzzle_input[2:]+[""])
        self.num_boards = len(self.boards.keys())
        self.board_width, self.board_height = len(self.boards[0][0]), len(self.boards[0])
        self.scores = {i:[[False for _ in range(self.board_width)] for __ in range(self.board_height)] for i in range(self.num_boards)} 

    def get_boards(self, puzzle_input):
        boards = defaultdict(list)
        idx = 0
        for line in puzzle_input:
            if line:
                values = [int(v) for v in line.split(" ") if v]
                boards[idx].append(values)
            else:
                idx+=1
        return boards 
                
    def get_final_score(self):
        
        for num in self.numbers:
            for idx, board in self.boards.items():
                for y, row in enumerate(board):
                    for x, value in enumerate(row):
                        if num == value:
                            self.scores[idx][y][x] = True    
                            bingo_value = self.get_if_bingo(idx, x, y, value)
                            if bingo_value:
                                return bingo_value

    def get_if_bingo(self, idx, x, y, value):
        scores = self.scores[idx]
        row_complete = all(scores[y])
        col_complete = all([row[x] for row in scores])
        if row_complete or col_complete:
            board = self.boards[idx]
            unmarked_mask = np.ma.masked_array(np.array(board), mask=np.array(scores))
            sum_unmarked_values = unmarked_mask.sum()
            return value*sum_unmarked_values
        return None
        
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        squid_bingo = SquidBingo(puzzle_input)
        print(f"Solution to first problem: {squid_bingo.get_final_score()}")