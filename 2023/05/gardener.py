
"""Solutions to https://adventofcode.com/2023/day/5 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path

number_pattern = re.compile(r"(\d+)")

def min_plant_location(mapping: dict, almanac: "list[str]"):
    for line in almanac:
        values = number_pattern.findall(line)
        if values:
            dest_start, source_start, map_range = [int(val) for val in values]
            for source_val in mapping.keys():
                source_end = source_start + map_range
                # update the dest values using the map if values are in range.
                if source_val >= source_start and source_val <= source_end:
                    dest_value = dest_start + (source_val - source_start)
                    mapping[source_val] = dest_value
        
        else:
            # make dest_values the new source values
            mapping = {val:val for val in list(mapping.values())} 
    return min(list(mapping.values()))

def gardener(almanac: "list[str]"):
    """Returns lowest location number that corresponds to any of the initial seed numbers

    seeds: 79 14 55 13
    
    seed-to-soil map:
    50 98 2
    52 50 48
    
    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15
    
    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4
    
    water-to-light map:
    88 18 7
    18 25 70
    
    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13
    
    temperature-to-humidity map:
    0 69 1
    1 0 69
    
    humidity-to-location map:
    60 56 37
    56 93 4
    
    The values describe a mapping between destination_range_start, source_range_start, and a range length of the previous value to the next.
    Values that fall outside of the ranges described have the same destination value as their own values.
    In this example the lowest location number is 35."""
    
    mapping = {int(val):int(val) for val in number_pattern.findall(almanac[0])}
    return min_plant_location(mapping, almanac[1:])
    
    # extract all numbers


if __name__ == "__main__":
    almanac_input_path = Path("almanac.txt")
    with open(almanac_input_path) as almanac_file:

        almanac_input = almanac_file.readlines()
        print(f"First Seed to Plant: {gardener(almanac_input)}")