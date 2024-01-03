"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from crates import Crates
class TestCrates(unittest.TestCase):


    puzzle_input = ["    [D]    ",
                    "[N] [C]    ",
                    "[Z] [M] [P]",
                    " 1   2   3 ",
                    "",
                    "move 1 from 2 to 1",
                    "move 3 from 1 to 3",
                    "move 2 from 2 to 1",
                    "move 1 from 1 to 2",
                    ]

    def test_part_one(self):
        expected_result = "CMZ"
        crates = Crates(self.puzzle_input)
        crates.rearrange()
        self.assertEqual(crates.top_crates(), expected_result)

    
    def test_part_two(self):
        expected_result = "MCD"
        crates = Crates(self.puzzle_input)
        crates.rearrange(save_order=True)
        self.assertEqual(crates.top_crates(), expected_result)