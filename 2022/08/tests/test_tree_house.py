"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from tree_house import TreeHouse
class TestTreeHouse(unittest.TestCase):

    puzzle_input = ["30373",
                    "25512",
                    "65332",
                    "33549",
                    "35390",]

    def test_part_one(self):
        tree_house = TreeHouse(self.puzzle_input)
        expected_result = 21
        self.assertEqual(tree_house.count_visible_trees(), expected_result)

    
    def test_part_two(self):
        tree_house = TreeHouse(self.puzzle_input)
        expected_result = 8
        self.assertEqual(tree_house.highest_sceneic_score(), expected_result)