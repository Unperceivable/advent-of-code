# %%
"""Solutions to https://adventofcode.com/2023/day/19 Puzzles."""
import re
from pathlib import Path
from collections import namedtuple
import sys

Part = namedtuple('Part', ["x", "m", "a", "s"])
    

class Workflows():
    def __init__(self, puzzle_input: "list[str]"):

        workflows = True
        workflow_list = []
        part_list = []
        for line in puzzle_input:
            if line == "":
                workflows = False    
            elif workflows:
                workflow_list.append(line)
            else:
                part_list.append(line)
        
        self.parts = self.extract_parts(part_list)
        self.workflows = self.extract_workflows(workflow_list)

        self.valid_branches = []

    def extract_parts(self, part_list): 
        parts = []
        part_pattern = re.compile(r"(\d+)")
        for part_line in part_list:
            groups = part_pattern.findall(part_line)
            part = Part(*[int(_) for _ in groups])
            parts.append(part)
        return parts

    def extract_workflows(self, workflow_list):
        pattern = re.compile(r'(\w+){([^{}]+)}')
        workflows = {}
        for workflow_line in workflow_list:
            match = pattern.match(workflow_line)
            if match:
                groups = [match.group(1)]
                inner_content = match.group(2)
                inner_groups = re.findall(r'(\w+[<>]\d+|\w+)', inner_content)
                groups.extend(inner_groups)
                
                workflow = {k:v for k,v in zip(groups[1:-1:2], groups[2:-1:2])}
                workflow.update({False:groups[-1]})
                workflows[groups[0]] = workflow
        return workflows
    
        
    def sort_parts(self):
        self.accepted_parts = []
        for part in self.parts:
            outcome = None
            workflow_key = "in"
            while workflow_key not in ["A", "R"]:
                workflow = self.workflows.get(workflow_key)
                for rule, flow in workflow.items():
                    if rule:
                        outcome = eval(f"part.{rule}")
                    
                    workflow_key = flow
                    if outcome:
                        break

                if workflow_key == "A":
                    self.accepted_parts.append(part)

    def sum_part_ratings(self):
        sum_part_ratings = 0
        for part in self.accepted_parts:
            sum_part_ratings += sum(part)
        return sum_part_ratings

    def generate_combinations(self, input_list):
        paths = []
        for i in range(len(input_list)):
            path = [f"!{k}" for k in input_list[:i]]        
            if input_list[i]:
                path.append(input_list[i])
            paths.append(path)
        return paths


    def set_valid_branches(self, key="in", current_path=[]):
        keys = [k for k in self.workflows[key].keys()]
        values = [v for v in self.workflows[key].values()]
        new_keys = self.generate_combinations(keys)
        for key, val in zip(new_keys, values):
            next_path = current_path[:]
            next_path.extend(key)
            if val in list(self.workflows.keys()):
                self.set_valid_branches(val, next_path)
            elif val == "A":
                self.valid_branches.append(next_path)
                # return next_path
            elif val == "R":
                pass

    def max_combinations(self):
        
        combinations = []
        for branch in self.valid_branches:
            limit = {"x":[1,4000], "m": [1,4000], "a": [1,4000], "s":[1,4000]}
            letter, symbol, number = None, None, None
            for sub_branch in branch:
                values = re.match(r'([!]?)(\w)([<>])(\d+)', sub_branch)
                
                negation = values.group(1)
                letter = values.group(2)
                symbol = values.group(3)
                number = int(values.group(4))

                if negation == "!":
                    if symbol == ">":
                        number+=1
                        symbol = "<"
                    elif symbol == "<":
                        number-=1
                        symbol = ">"
                    
                if "<" in symbol:
                    new_limit = number-1
                    limit[letter][1] = new_limit
                elif ">" in symbol:
                    new_limit = number+1
                    limit[letter][0] = new_limit
                else:
                    raise ValueError("Unexpected Value")

            num_combinations = 1
            for val_range in limit.values():
                _min, _max = val_range[0], val_range[1]
                range = _max - _min +1 
                num_combinations *= range
            
            combinations
            combinations.append(num_combinations)
        return sum(combinations)
            

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        workflows = Workflows(puzzle_input)
        workflows.sort_parts()
        rating = workflows.sum_part_ratings()
        print(f"Solution to first problem: {rating}")
        workflows.set_valid_branches()
        print(f"Solution to second problem: {workflows.max_combinations()}")