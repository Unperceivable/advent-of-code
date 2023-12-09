"""Tests for https://adventofcode.com/2023/day/8 Puzzles."""

import unittest
from extrapolate import extrapolate
class TestExtrapolate(unittest.TestCase):

    def test_part_one(self):
        """."""
        map_input = ["0 3 6 9 12 15",
                    "1 3 6 10 15 21",
                    "10 13 16 21 30 45",]
        expected_result = 114
        
        self.assertEqual(extrapolate(map_input), expected_result)
        
    def test_part_two(self):
        """."""
        map_input = ["0 3 6 9 12 15",
                    "1 3 6 10 15 21",
                    "10 13 16 21 30 45",]
        expected_result = 2
        
        self.assertEqual(extrapolate(map_input, reverse=True), expected_result)