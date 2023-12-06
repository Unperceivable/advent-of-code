
"""Solutions to https://adventofcode.com/2023/day/6 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path


class BoatRace(namedtuple('BoatRace', ["time", "record"])):
    """Cube Conundrum Game."""
    def number_of_wins(self):
        num_of_wins = 0
        for val in range(1,self.time-1):
            if (self.time-val)*val > self.record:
                num_of_wins += 1
        return num_of_wins

def boat_race(boat_race: "list[str]"):
    """Returns the product of number of ways to win for each race

    Time:      7  15   30
    Distance:  9  40  200
    
    Time is the length of the race, distance is the goal to beat.
    For each unit of time waited speed increases by 1, the goal is product of the number of possible ways to win each race. 
    In this case it is 288 (4 * 8 * 9)."""
    
    
    # extract all numbers
    number_pattern = re.compile(r"(\d+)")
    
    race_time = [int(time) for time in number_pattern.findall(boat_race[0])]
    race_record = [int(dist) for dist in number_pattern.findall(boat_race[1])]

    product_of_wins = 1
    for time, record in zip(race_time, race_record):
        num_of_wins = BoatRace(time,record).number_of_wins()
        product_of_wins *= num_of_wins

    return product_of_wins

def kerning_boat_race(boat_race: "list[str]"):
    """Returns the product of number of ways to win the race

    Time:      7  15   30
    Distance:  9  40  200
    
    Time is the length of the race, distance is the goal to beat
    For each unit of time waited speed increases by 1, the goal is product of the number of possible ways to win each race. 
    In this case it is 288 (4 * 8 * 9)."""
    
    
    # extract all numbers
    number_pattern = re.compile(r"(\d+)")
    
    race_time = int("".join(number_pattern.findall(boat_race[0])))
    race_record = int("".join(number_pattern.findall(boat_race[1])))  

    return BoatRace(race_time,race_record).number_of_wins()

if __name__ == "__main__":
    boat_race_input_path = Path("boat_race.txt")
    with open(boat_race_input_path) as boat_race_file:

        boat_race_input = boat_race_file.readlines()
        print(f"Product of number of possible wins: {boat_race(boat_race_input)}")
        print(f"Number possible wins for long race: {kerning_boat_race(boat_race_input)}")