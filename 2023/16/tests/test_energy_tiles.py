"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from energy_tiles import EnergyTiles
class TestEnergyTiles(unittest.TestCase):

    def test_part_one(self):
        """."""
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
        expected_result = 46
        energy_tiles = EnergyTiles(puzzle_input)
        energy_tiles.energize_tiles()
        self.assertEqual(energy_tiles.count_energized(), expected_result)

    def test_part_two(self):
        """."""
        pass