# %%
import re
from pathlib import Path
from collections import namedtuple

class MonkeyBusiness():
    def __init__(self, puzzle_input: "list[str]"):
        self.monkey_idx_pattern = re.compile(r"Monkey (\d+)")
        self.num_pattern = re.compile(r"(\d+)")
        self.operation_pattern = re.compile(r"([*+-] [\d|\w]+)")
        self.monkies = self.get_monkies(puzzle_input)
        self.num_cycles = 20
    
    def get_monkies(self, monkey_notes):
        start = 0
        monkies = {}
        for start in range(0,len(monkey_notes)//7 +1):
            monkey_note = monkey_notes[start*7:(start+1)*7]
            monkey_idx = int(self.monkey_idx_pattern.match(monkey_note[0]).group(1))
            items = [int(i) for i in self.num_pattern.findall(monkey_note[1])]
            operation = self.operation_pattern.search(monkey_note[2]).group(0)
            action = self.get_action(monkey_note)
            monkies[monkey_idx] = {"items":items, "inspections":0, "op":operation, "action":action} 

        return monkies

    def get_action(self, monkey_note):
        action_value = int(self.num_pattern.search(monkey_note[3]).group(1))
        action_true = int(self.num_pattern.search(monkey_note[4]).group(1))
        action_false = int(self.num_pattern.search(monkey_note[5]).group(1))
        return {action_value: {True: action_true, False:action_false}}
    
    def get_level(self):
        num_inspections = [self.monkies[idx]["inspections"] for idx in self.monkies.keys()]
        first, second = sorted(num_inspections, reverse=True)[:2]
        return first*second
    
    def observe(self):
        for cycle in range(self.num_cycles):
            for monkey_idx in self.monkies.keys():
                for _ in range(len(self.monkies[monkey_idx]["items"])):
                    item = self.monkies[monkey_idx]["items"].pop()
                    new_item_value = self.monkey_inspection(monkey_idx, item)
                    new_item_value =  new_item_value // 3
                    self.monkies[monkey_idx]["inspections"] += 1

                    action_value = list(self.monkies[monkey_idx]["action"].keys())[0]
                    action_result = not bool(new_item_value % action_value)
                    other_monkey_idx = self.monkies[monkey_idx]["action"][action_value][action_result]

                    self.monkies[other_monkey_idx]["items"].append(new_item_value)

    def monkey_inspection(self, idx, item_value):
        operation = self.monkies[idx]["op"]
        if "old" in operation:
            operation = f"{item_value} {operation[0]} {item_value}"
        else:
            operation = f"{item_value} {operation}"
        new_value = eval(operation)
        return new_value
        
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        monkey_business = MonkeyBusiness(puzzle_input)
        monkey_business.observe()
        print(f"Solutions to first problem: {monkey_business.get_level()}")