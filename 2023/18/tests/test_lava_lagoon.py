"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from lava_lagoon import LavaLagoon
class TestLavaLagoon(unittest.TestCase):

    def test_part_one(self):
        """."""
        
        puzzle_input = ["R 6 (#70c710)",
                        "D 5 (#0dc571)",
                        "L 2 (#5713f0)",
                        "D 2 (#d2c081)",
                        "R 2 (#59c680)",
                        "D 2 (#411b91)",
                        "L 5 (#8ceee2)",
                        "U 2 (#caa173)",
                        "L 1 (#1b58a2)",
                        "U 2 (#caa171)",
                        "R 2 (#7807d2)",
                        "U 3 (#a77fa3)",
                        "L 2 (#015232)",
                        "U 2 (#7a21e3)",]
        expected_result = 62
        lava_lagoon = LavaLagoon(puzzle_input)
        lava_lagoon.dig_lagoon()
        lava_count = lava_lagoon.count_lava()
        self.assertEqual(lava_count, expected_result)

    def test_part_two(self):
        """."""
        pass