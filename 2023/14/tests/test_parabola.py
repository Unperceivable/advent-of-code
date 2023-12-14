"""Tests for https://adventofcode.com/2023/day/14 Puzzles."""

import unittest
from parabola import Parabola
class TestHotSprings(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = ["O....#....",
                        "O.OO#....#",
                        ".....##...",
                        "OO.#O....O",
                        ".O.....O#.",
                        "O.#..O.#.#",
                        "..O..#O..O",
                        ".......O..",
                        "#....###..",
                        "#OO..#....",]

        expected_result = 136
        self.assertEqual(Parabola(puzzle_input).north_total_load(), expected_result)
