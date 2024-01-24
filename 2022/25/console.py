from pathlib import Path
import math

class Console():
    def __init__(self, puzzle_input: "list[str]"):
        self.digit_map = {"2":2, "1":1, "0":0, "-":-1, "=":-2}
        self.snafu_digits = [[self.digit_map[c] for c in line] for line in puzzle_input]

    def decimal_to_snafu(self, decimal):
        remainder = decimal
        num_digits  = int(math.log(decimal,5))
        snafu_map = {2:"2", 1:"1", 0:"0", -1:"-", -2:"="}
        snafu = ""
        for digit in range(num_digits,-1,-1):
            decimal_value = int(5**digit)    
            digit_value = round(remainder/decimal_value)
            snafu += snafu_map[digit_value]
            remainder -= decimal_value * digit_value
        return snafu 


    def sum_snafu_numbers(self):
        total_sum = 0
        for snafu in self.snafu_digits:
            subtotal = 0 
            for power, digit in enumerate(snafu[::-1]):
                subtotal += digit*5**power
            total_sum += subtotal
            
        return self.decimal_to_snafu(total_sum) 

        
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        console = Console(puzzle_input)
        print(f"Solution to first problem: {console.sum_snafu_numbers()}")