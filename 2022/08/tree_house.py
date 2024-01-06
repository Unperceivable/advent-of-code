# %%
import re
from pathlib import Path
from collections import defaultdict
import numpy as np
class TreeHouse():
    
    def __init__(self, puzzle_input: "list[str]"):
        self.forest = np.array([[int(c) for c in row] for row in puzzle_input])
        self.forest_width = len(self.forest[0])
        self.forest_height = len(self.forest)
        self.perimeter = 2*self.forest_width + 2*self.forest_height - 4

    def get_views(self, x,y):
        above = self.forest[:x, y]
        below = self.forest[x+1:, y]
        left_of = self.forest[x, :y]
        right_of = self.forest[x,y+1:]
        views = [above[::-1], below, left_of[::-1], right_of]
        return views

    
    def count_visible_trees(self):
        count_visible_trees = self.perimeter
        for x in range(1, self.forest_width-1):
            for y in range(1, self.forest_height-1):
                tree_height = self.forest[x,y]
                views = self.get_views(x,y)
                visible = any([np.all(dir < tree_height) for dir in views])
                if visible:
                    count_visible_trees +=1
        return count_visible_trees
    
    def highest_sceneic_score(self):
        max_scenic_score = 0
        for x in range(0, self.forest_width):
            for y in range(0, self.forest_height):
                scenic_score = 1
                tree_height = self.forest[x,y]
                views = self.get_views(x,y)
                for view in views:
                    score = 0
                    if view.size > 0:
                        higher_trees = np.where(view >= tree_height)[0].flat
                        if higher_trees:
                            score = higher_trees[0]+1
                        else:
                            score = view.shape[0]
                        scenic_score *= score
                    else:
                        scenic_score *= score
                max_scenic_score = max(max_scenic_score, scenic_score)
        return max_scenic_score
                
         
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        tree_house = TreeHouse(puzzle_input)
        print(f"Solutions to first problem: {tree_house.count_visible_trees()}")
        print(f"Solutions to second problem: {tree_house.highest_sceneic_score()}")