import unittest
from falling_sand import FallingSand
class TestFallingSand(unittest.TestCase):

    puzzle_input = ["498,4 -> 498,6 -> 496,6",
                    "503,4 -> 502,4 -> 502,9 -> 494,9",]

    def test_part_one(self):
        falling_sand = FallingSand(self.puzzle_input)
        expected_result = 24
        self.assertEqual(falling_sand.max_sand(), expected_result)

    
    def test_part_two(self):
        pass