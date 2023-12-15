# %%
"""Solutions to https://adventofcode.com/2023/day/15 Puzzles."""
import re
from pathlib import Path
from collections import defaultdict

class LensLibrary():
    
    def __init__(self, input: "list[str]"):
        if isinstance(input, str):
            input = input.split(",")
        self.input = input
        self.factor = 17
        self.modulus = 256

    def sum_of_lens_libraryes(self):
        sum_of_lens_libraryes = 0
        for word in self.input:
            sum_of_lens_libraryes += self.lens_library_word(word)
        return sum_of_lens_libraryes 
        
    def lens_library_word(self, word):
        """Return numeric lens_library for word.
        
        Example: HASH
        
        Determine the ASCII code for the current character of the string.
        Increase the current value by the ASCII code you just determined.
        Set the current value to itself multiplied by 17.
        Set the current value to the remainder of dividing itself by 256.
        
        Result for word is 52."""

        lens_library_value = 0
        for char in word:
            lens_library_value += ord(char)
            lens_library_value *= self.factor 
            lens_library_value %= self.modulus
        
        return lens_library_value

    def calc_focusing_power(self):
        lens_map = defaultdict(dict)
        step_pattern = re.compile(r"(\w+)([=-])(\d)?")
        for step in self.input:
            match = step_pattern.match(step)
            label = match.group(1)
            lens_library = self.lens_library_word(label)
            operation = match.group(2)
            
            if operation == "=":
                lens = int(match.group(3))
                lens_map[lens_library][label] = lens
            else:
                if lens_map[lens_library].get(label, None):
                    lens_map[lens_library].pop(label)
 
        return self.focusing_power(lens_map)

    def focusing_power(self, lens_map):
       sum_focusing_power = 0 
       for num, box in lens_map.items():
            focus_power = sum([(dist+1)*lens for dist, lens in enumerate(list(box.values()))])
            sum_focusing_power += (num+1)*focus_power
       
       return sum_focusing_power

# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read()
        lens_library = LensLibrary(puzzle_input)
        print(f"Solution to first problem: {lens_library.sum_of_lens_libraryes()}")
        print(f"Solution to first problem: {lens_library.calc_focusing_power()}")
        
