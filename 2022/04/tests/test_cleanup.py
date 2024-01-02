"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from cleanup import Cleanup
class TestCleanup(unittest.TestCase):


    puzzle_input = ["2-4,6-8",
                    "2-3,4-5",
                    "5-7,7-9",
                    "2-8,3-7",
                    "6-6,4-6",
                    "2-6,4-8",]

    def test_part_one(self):
        expected_result = 2
        cleanup = Cleanup(self.puzzle_input)
        self.assertEqual(cleanup.sum_full_subranges(), expected_result)
    
    def test_part_two(self):
        expected_result = 4
        cleanup = Cleanup(self.puzzle_input)
        self.assertEqual(cleanup.sum_partial_subranges(), expected_result)