"""Tests for https://adventofcode.com/2023/day/13 Puzzles."""

import unittest
from mirror_valley import MirrorValley
class TestMirrorValley(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = ["#.##..##.",
                        "..#.##.#.",
                        "##......#",
                        "##......#",
                        "..#.##.#.",
                        "..##..##.",
                        "#.#.##.#.",
                        "",
                        "#...##..#",
                        "#....#..#",
                        "..##..###",
                        "#####.##.",
                        "#####.##.",
                        "..##..###",
                        "#....#..#",]

        expected_result = 405
        self.assertEqual(MirrorValley(puzzle_input).sum_of_reflections(), expected_result)

    def test_part_two(self):
        puzzle_input = ["#.##..##.",
                        "..#.##.#.",
                        "##......#",
                        "##......#",
                        "..#.##.#.",
                        "..##..##.",
                        "#.#.##.#.",
                        "",
                        "#...##..#",
                        "#....#..#",
                        "..##..###",
                        "#####.##.",
                        "#####.##.",
                        "..##..###",
                        "#....#..#",]

        expected_result = 400
        self.assertEqual(MirrorValley(puzzle_input, smudged=True).sum_of_reflections(), expected_result)