"""Tests for https://adventofcode.com/2023/day/11 Puzzles."""

import unittest
from hot_springs import HotSprings
class TestHotSprings(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = ["???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",]

        expected_result = 21
        self.assertEqual(HotSprings(puzzle_input).sum_of_arrangements(), expected_result)

    def test_part_two(self):
       pass 