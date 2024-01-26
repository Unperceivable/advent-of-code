import unittest
from dive import Dive
class TestDive(unittest.TestCase):

    puzzle_input = ["forward 5",
                    "down 5",
                    "forward 8",
                    "up 3",
                    "down 8",
                    "forward 2",]


    def test_part_one(self):
        dive = Dive(self.puzzle_input)
        expected_result = 150
        self.assertEqual(dive.get_dive_length(), expected_result)
    
    def test_part_two(self):
        dive = Dive(self.puzzle_input)
        expected_result = 900
        self.assertEqual(dive.get_dive_length(inverted=True), expected_result)