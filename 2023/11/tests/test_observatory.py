"""Tests for https://adventofcode.com/2023/day/11 Puzzles."""

import unittest
from observatory import Observatory
class TestObservatory(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = ["...#......",
                        ".......#..",
                        "#.........",
                        "..........",
                        "......#...",
                        ".#........",
                        ".........#",
                        "..........",
                        ".......#..",
                        "#...#....."]

        expected_result = 374
        self.assertEqual(Observatory(puzzle_input).sum_of_galaxy_dists(), expected_result)

    def test_part_two(self):
        
        puzzle_input = ["...#......",
                        ".......#..",
                        "#.........",
                        "..........",
                        "......#...",
                        ".#........",
                        ".........#",
                        "..........",
                        ".......#..",
                        "#...#....."]

        expected_result = 1030
        self.assertEqual(Observatory(puzzle_input, expansion_factor=10).sum_of_galaxy_dists(), expected_result)
        expected_result = 8410
        self.assertEqual(Observatory(puzzle_input, expansion_factor=100).sum_of_galaxy_dists(), expected_result)