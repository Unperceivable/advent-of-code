"""Solutions to https://adventofcode.com/2023/day/2 Puzzles."""

import re
from collections import namedtuple
from pathlib import Path

game_pattern = re.compile(r"Game (\d+)")
red_pattern = re.compile(r"(\d+) red")
green_pattern = re.compile(r"(\d+) green")
blue_pattern = re.compile(r"(\d+) blue")

class Game(namedtuple('Game', ["id", "red", "green", "blue"])):
    """Cube Conundrum Game."""
    def __le__(self, other):
        """Return game id if all values are less than or equal to the other game."""
        red_le = self.red <= other.red
        green_le = self.green <= other.green
        blue_le =  self.blue <= other.blue
        if red_le and green_le and blue_le:
            return self.id
        else:
            return 0

    def power(self):
        """Calculates power of game r*g*b."""
        return self.red * self.green * self.blue

def cube_conundrum(conundrum_text: list[str], sample_game: Game):
    """Calculate the the sum of the IDs of cube conundrum games.

    For example:

    Number of possible games with sample game of 12 red cubes, 13 green cubes, and 14 blue cubes.

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    Games 1, 2, and 5 would have been possible, sum of these IDs returns 8."""
    
    sum_game_ids = 0
    for line in conundrum_text:
        game_id = int(game_pattern.search(line).group(1))
        red_max = max([int(_) for _ in red_pattern.findall(line)])       
        green_max = max([int(_) for _ in green_pattern.findall(line)])       
        blue_max = max([int(_) for _ in blue_pattern.findall(line)])       

        current_game = Game(game_id, red_max, green_max, blue_max)
        sum_game_ids += (current_game <= sample_game)

    return sum_game_ids
        
def min_power_cube_conundrum(conundrum_text: list[str]):
    """Calculate the the min power of all games.

    For example:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
    The power of the minimum set of cubes for each game are 48, 12, 1560, 630, and 36, a sum of 2286."""
    
    sum_min_game_powers = 0
    for line in conundrum_text.readlines():
        game_id = int(game_pattern.search(line).group(1))
        red_max = max([int(_) for _ in red_pattern.findall(line)])       
        green_max = max([int(_) for _ in green_pattern.findall(line)])       
        blue_max = max([int(_) for _ in blue_pattern.findall(line)])       

        current_game = Game(game_id, red_max, green_max, blue_max)
        sum_min_game_powers += current_game.power()

    return sum_min_game_powers

if __name__ == "__main__":
    cube_conundrum_text_path = Path("cube_conundrum.txt")
    with open(cube_conundrum_text_path) as cube_conundrum_text:

        sample_game = Game(0, 12, 13, 14)
        # print(f"Cube Conundrum: {cube_conundrum(cube_conundrum_text, sample_game)}")
        print(f"Min Power Cube Conundrum: {min_power_cube_conundrum(cube_conundrum_text)}")