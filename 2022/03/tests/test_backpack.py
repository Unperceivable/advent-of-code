"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from backpack import Backpack
class TestBackpack(unittest.TestCase):


    puzzle_input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
                    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                    "PmmdzqPrVvPwwTWBwg",
                    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                    "ttgJtRGJQctTZtZT",
                    "CrZsJsPPZsGzwwsLwLmpwMDw",]

    def test_part_one(self):
        expected_result = 157
        backpack = Backpack(self.puzzle_input)
        self.assertEqual(backpack.sum_priorities(), expected_result)

    def test_part_two(self):
        expected_result = 70
        backpack = Backpack(self.puzzle_input)
        self.assertEqual(backpack.badge_priorities(), expected_result)