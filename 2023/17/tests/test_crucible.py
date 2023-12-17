"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from crucible import Crucible
class TestCrucible(unittest.TestCase):

    def test_part_one(self):
        """."""
        
        puzzle_input = ["2413432311323",
                        "3215453535623",
                        "3255245654254",
                        "3446585845452",
                        "4546657867536",
                        "1438598798454",
                        "4457876987766",
                        "3637877979653",
                        "4654967986887",
                        "4564679986453",
                        "1224686865563",
                        "2546548887735",
                        "4322674655533",]
        expected_result = 102
        crucible = Crucible(puzzle_input)
        crucible.best_path()
        self.assertEqual(crucible.heatloss, expected_result)

    def test_part_two(self):
        """."""
        pass