"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from energy_tiles import EnergyTiles
class TestEnergyTiles(unittest.TestCase):

    puzzle_input = [".|...\....",
                    "|.-.\.....",
                    ".....|-...",
                    "........|.",
                    "..........",
                    ".........\\",
                    "..../.\\\\..",
                    ".-.-/..|..",
                    ".|....-|.\\",
                    "..//.|....",]
    energy_tiles = EnergyTiles(puzzle_input)

    def test_part_one(self):
        expected_result = 46
        energized_tiles = self.energy_tiles.energize_tiles()
        self.assertEqual(energized_tiles, expected_result)

    def test_part_two(self):
        expected_result = 51
        max_energizeable = self.energy_tiles.max_energizeable()
        self.assertEqual(max_energizeable, expected_result)
