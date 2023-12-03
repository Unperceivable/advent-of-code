"""Trebuchet Tests."""
import unittest
from cube_conundrum import Game, cube_conundrum, min_power_cube_conundrum

class TestCubeConundrum(unittest.TestCase):

    conundrum_text = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    def test_cube_conundrum(self):
        """cube conundrum test, sample data from https://adventofcode.com/2023/day/1."""
        sample_game = Game(0, 12, 13, 15)
        self.assertEqual(cube_conundrum(self.conundrum_text, sample_game), 8)

    def test_min_power_cube_conundrum(self):
        """cube conundrum test, sample data from https://adventofcode.com/2023/day/1."""
        self.assertEqual(min_power_cube_conundrum(self.conundrum_text), 2286)

if __name__ == "__main__":
    unittest.main()