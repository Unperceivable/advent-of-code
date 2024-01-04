"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from tuning import Tuning
class TestTuning(unittest.TestCase):


    puzzle_inputs = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
                    "bvwbjplbgvbhsrlpgdmjqwftvncz",
                    "nppdvjthqldpwncqszvftbrmjlhg",
                    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",]

    def test_part_one(self):
        for puzzle_input, expected_result in zip(self.puzzle_inputs,[7,5,6,10,11]):
            tuning = Tuning(puzzle_input)
            self.assertEqual(tuning.get_marker(), expected_result)

    
    def test_part_two(self):
        for puzzle_input, expected_result in zip(self.puzzle_inputs,[19,23,23,29,26]):
            tuning = Tuning(puzzle_input)
            self.assertEqual(tuning.get_marker(msg_len=14), expected_result)