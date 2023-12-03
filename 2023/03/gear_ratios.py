"""Solutions to https://adventofcode.com/2023/day/3 Puzzles."""
import re
from collections import namedtuple, defaultdict
from pathlib import Path
from functools import reduce


number_pattern = re.compile(r"\d+")
special_pattern = re.compile(r"[^0-9.\n]")
gear_pattern = re.compile(r"\*")

GearedNumber = namedtuple('GearedNumber', ["value", "gear_line", "gear_pos"])

class LocatedNumber(namedtuple('LocatedNumber', ["value", "line", "start", "end"])):
    def gear_list(self, engine_schematic: list[str]):
        """Returns list of GearedNumbers."""
        min_row = max(0,self.line-1)
        max_row = min(len(engine_schematic)-1, self.line+1)
        max_length = len(engine_schematic[0])-1
        raster_start = max(0, self.start -1)
        raster_end = min(max_length, self.end)
        gear_list = []
        for row in range(min_row,max_row+1):
            raster_values = engine_schematic[row][raster_start:raster_end+1]
            for match in re.finditer(gear_pattern, raster_values):
               geared_number = GearedNumber(self.value, row, raster_start + match.start())
               gear_list.append(geared_number)
        return gear_list
        
    def has_adjacent_symbol(self, engine_schematic: list[str]):
        """Returns bool if LocatedNumber is adjacent to a symbol."""
        min_row = max(0,self.line-1)
        max_row = min(len(engine_schematic)-1, self.line+1)
        max_length = len(engine_schematic[0])-1
        raster_start = max(0, self.start -1)
        raster_end = min(max_length, self.end)
        adjacent_values = ""
        for row in range(min_row,max_row+1):
            raster_values = engine_schematic[row][raster_start:raster_end+1]
            adjacent_values += raster_values
        
        has_adjacent_value = special_pattern.search(adjacent_values)
        if has_adjacent_value:
            return True
        else:
            return False


def valid_parts(engine_schematic: list[str]):
    """Adds up all the part numbers adjacent to a symbol from an engine schematic.
    
    example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.. 
    
    Every number except 114 and 58 is summed equaling 4361
    """
    
    sum_of_valid_parts = 0
    for line_number, line in enumerate(engine_schematic):
        for match in re.finditer(number_pattern, line):
            start = match.start()
            end = match.end()
            current_number = LocatedNumber(int(match.group()), line_number, start, end)
            if current_number.has_adjacent_symbol(engine_schematic):
                sum_of_valid_parts += current_number.value

    
    return sum_of_valid_parts

def gear_ratios(engine_schematic: list[str]):
    """Sums  all of the gear ratios in an engine schematic.
    
    example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.. 
    
    A gear is any * adjacent to exactly two part numbers which get multiplied to form a gear ratio.
    The sum of gear ratios is 467835 in this example.
    """
    
    sum_of_valid_parts = 0
    geared_numbers = []
    for line_number, line in enumerate(engine_schematic):
        for match in re.finditer(number_pattern, line):
            start = match.start()
            end = match.end()
            current_number = LocatedNumber(int(match.group()), line_number, start, end)
            geared_numbers.extend(current_number.gear_list(engine_schematic))
    gear_groups = defaultdict(list)
    for gn in geared_numbers:
        gear_groups[(gn.gear_line, gn.gear_pos)].append(gn.value)

    # only allow exactly two values per gear
    gear_groups = {k:v for k,v in gear_groups.items() if len(v) == 2}
    gear_ratios = [reduce(lambda x, y: x * y, values) for _, values in gear_groups.items()]
    return sum(gear_ratios)
    
if __name__ == "__main__":
    engine_schematic_path = Path("engine_schematic.txt")
    with open(engine_schematic_path) as engine_schematic_file:
        engine_schematic = engine_schematic_file.readlines()
        print(f"Valid Parts: {valid_parts(engine_schematic)}")
        print(f"Gear Ratios: {gear_ratios(engine_schematic)}")