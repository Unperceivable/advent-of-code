# %%
import re
from pathlib import Path
from collections import namedtuple

class RopeBridge():
    def __init__(self, puzzle_input: "list[str]", tail_length=1):
        self.moves = puzzle_input
        self.tail_length = tail_length
        self.rope_length = 1 + self.tail_length
        self.rope = self.rope_length*[(0,0)]
        self.tail_poses = {(0,0)}
        self.min_x,self.max_x,self.min_y,self.max_y = 0,0,0,0
    
    def move_rope(self):
        for move in self.moves:
            move_pattern = re.compile("(\w) (\d+)")
            match = move_pattern.match(move)
            dir, dist = match.group(1), int(match.group(2))
            for _ in range(dist):
                self.update_head(dir)
                for rope_idx in range(1, self.tail_length+1):
                    self.update_tail(rope_idx)
                self.tail_poses.add(self.rope[-1])

                self.min_x = min(self.min_x,self.rope[0][0])
                self.max_x = max(self.max_x,self.rope[0][0])
                self.min_y = min(self.min_y,self.rope[0][1])
                self.max_y = max(self.max_y,self.rope[0][1])
    
    def print(self):
        for y in range(self.min_y-1, self.max_y+1):
            for x in range(self.min_x, self.max_x+2):    
                char = "."
                for idx, rope_part in enumerate(self.rope[1:-1], start=1):
                    if (x,y) == rope_part:
                        char = str(idx)
                        break
                if (x,y) == self.rope[-1]:
                    char = "T"
                if (x,y) == self.rope[0]:
                    char = "H"
                print(char, end="")
            print()
                
    def update_head(self, dir):
        x,y = self.rope[0]
        if dir == "U":
            y -= 1 
        elif dir == "D":
            y += 1
        elif dir == "L":
            x -= 1
        elif dir == "R":
            x += 1
        self.rope[0] = (x,y)

    def update_tail(self, rope_idx):
        x,y = self.rope[rope_idx]
        head_x, head_y = self.rope[rope_idx-1]

        diff_x = head_x - x
        diff_y = head_y - y

        if abs(diff_y) == abs(diff_x) and abs(diff_y) >= 2:
            x += diff_x//2
            y += diff_y//2
        elif diff_y <= -2:
            y -= 1
            x = head_x
        elif diff_y >= 2:
            y += 1
            x = head_x
        elif diff_x <= -2:
            x -= 1
            y = head_y
        elif diff_x >= 2:
            x += 1
            y = head_y
        
        self.rope[rope_idx] = (x,y)

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        rope_bridge = RopeBridge(puzzle_input, tail_length=1)
        rope_bridge.move_rope()
        num_poses = len(rope_bridge.tail_poses)
        print(f"Solutions to first problem: {num_poses}")
        rope_bridge = RopeBridge(puzzle_input, tail_length=9)
        rope_bridge.move_rope()
        num_poses = len(rope_bridge.tail_poses)
        print(f"Solutions to second problem: {num_poses}")