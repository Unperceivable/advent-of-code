import unittest
from blizzard import Blizzard
class TestBlizzard(unittest.TestCase):

    puzzle_input = ["#.#####",
                    "#.....#",
                    "#>....#",
                    "#.....#",
                    "#...v.#",
                    "#.....#",
                    "#####.#",]

    def test_part_one(self):
        blizzard = Blizzard(self.puzzle_input)
        expected_result = 18
        self.assertEqual(blizzard.fewest_minutes(), expected_result)
    
    def test_part_two(self):
        pass