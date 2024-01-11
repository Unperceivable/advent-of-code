"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from distress_signal import DistressSignal
class TestDistressSignal(unittest.TestCase):

    puzzle_input = ["[1,1,3,1,1]",
                    "[1,1,5,1,1]",
                    "",
                    "[[1],[2,3,4]]",
                    "[[1],4]",
                    "",
                    "[9]",
                    "[[8,7,6]]",
                    "",
                    "[[4,4],4,4]",
                    "[[4,4],4,4,4]",
                    "",
                    "[7,7,7,7]",
                    "[7,7,7]",
                    "",
                    "[]",
                    "[3]",
                    "",
                    "[[[]]]",
                    "[[]]",
                    "",
                    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
                    "[1,[2,[3,[4,[5,6,0]]]],8,9]",]
    
    def test_part_one(self):
        distress_signal = DistressSignal(self.puzzle_input)
        expected_result = 13
        self.assertEqual(distress_signal.sum_of_indexes(), expected_result)

    
    def test_part_two(self):
        pass