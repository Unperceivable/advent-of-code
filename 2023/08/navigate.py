
"""Solutions to https://adventofcode.com/2023/day/8 Puzzles."""
import math
import re
from pathlib import Path

def build_mapping(map_input: "list[str]") -> dict:
    mapping = {}
    path_pattern = re.compile(r"(\w+) = \((\w+), (\w+)")
    # build map
    for line in map_input[2:]:
        match = path_pattern.search(line)
        mapping[match.group(1)] = {"L":match.group(2), "R":match.group(3)}
    return mapping
 
def navigate(map_input: "list(int)"):
    """Returns number of steps to get to the target ZZZ

    RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ) 
    
    Starting with AAA, you need to look up the next element based on RL instruction as input.
    By following the left/right instructions in this case you reach ZZZ in 2 steps."""

    
    mapping = build_mapping(map_input)

    start_pos = "AAA"
    target_pos = "ZZZ"
    current_pos = start_pos
    num_steps = 0

    instructions = map_input[0]
    while current_pos != target_pos:
        for direction in instructions:
            num_steps += 1
            next_pos = mapping[current_pos][direction]
            current_pos = next_pos
            if next_pos == target_pos:
                break

    return num_steps
    

def renavigate(map_input: "list(int)"):
    """Returns number of steps until all start nodes XXA lead to XXZ

    LR
    
    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    
    return number of steps until all starting threads end in a Z simultaneously following the pattern.
    So, in this example, you end up entirely on nodes that end in Z after 6 steps."""
    

    mapping = build_mapping(map_input)
    # solve 
    instructions = map_input[0]
    def solve_path(instructions, mapping, start_pos):
        num_steps = 0
        solved = False
        current_pos = start_pos
        while not solved:
            for direction in instructions:
                num_steps += 1
                next_pos = mapping[current_pos][direction]
                current_pos = next_pos
                solved = next_pos.endswith("Z")
                if solved:
                    break

        return num_steps
        
    start_positions = [pos for pos in list(mapping.keys()) if pos.endswith("A")]
    num_of_steps = [solve_path(instructions, mapping, pos) for pos in start_positions]
    print(num_of_steps)
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)

    def find_smallest_number_with_factors(factors):
        result = 1
        for factor in factors:
            result = lcm(result, factor)
        return result

    smallest_num_of_steps = find_smallest_number_with_factors(num_of_steps) 
    return smallest_num_of_steps

if __name__ == "__main__":    
    map_path = Path("map.txt")
    with open(map_path) as map_input_file:
        map_input = map_input_file.read().splitlines()
        print(f"Number of steps to escape: {navigate(map_input)}")
        print(f"Number of steps to escape: {renavigate(map_input)}")