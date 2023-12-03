"""Gear Ratio Tests."""

import unittest
from gear_ratios import gear_ratios, valid_parts
class TestGearRatio(unittest.TestCase):
    def test_valid_parts(self):
        

        engine_schematic = ["467..114..",
                            "...*......",
                            "..35..633.",
                            "......#...",
                            "617*......",
                            ".....+.58.",
                            "..592.....",
                            "......755.",
                            "...$.*....",
                            ".664.598..",]


        # self.assertEqual(valid_parts(engine_schematic), 4361)
    
    def test_gear_ratio(self):
        

        engine_schematic = ["467..114..",
                            "...*......",
                            "..35..633.",
                            "......#...",
                            "617*......",
                            ".....+.58.",
                            "..592.....",
                            "......755.",
                            "...$.*....",
                            ".664.598..",]


        self.assertEqual(gear_ratios(engine_schematic), 467835)