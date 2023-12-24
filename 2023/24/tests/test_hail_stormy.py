"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from hail_storm import HailStorm
class TestHailStorm(unittest.TestCase):


    puzzle_input = ["19, 13, 30 @ -2,  1, -2",
                    "18, 19, 22 @ -1, -1, -2",
                    "20, 25, 34 @ -2, -2, -4",
                    "12, 31, 28 @ -1, -2, -1",
                    "20, 19, 15 @  1, -5, -3",]

    def test_part_one(self):
        min_pos, max_pos = 7, 27
        hail_storm = HailStorm(self.puzzle_input, min_pos, max_pos)
        expected_result = 2
        self.assertEqual(hail_storm.get_2d_collisions(), expected_result)

    # def test_part_two(self):
    #     hail_storm = HailStorm(self.puzzle_input, slippery=False)
    #     expected_result = 154
    #     self.assertEqual(hail_storm.get_collisions(), expected_result)