"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from rock_paper_scissors import RockPaperScissors
class TestRockPaperScissors(unittest.TestCase):


    puzzle_input = ["A Y",
                    "B X",
                    "C Z",]

    def test_part_one(self):
        expected_result = 15
        rock_paper_scissors = RockPaperScissors(self.puzzle_input)
        self.assertEqual(rock_paper_scissors.play(strat="a"), expected_result)

    def test_part_two(self):
        expected_result = 12
        rock_paper_scissors = RockPaperScissors(self.puzzle_input)
        self.assertEqual(rock_paper_scissors.play(strat="b"), expected_result)