"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from calorie_count import CalorieCount
class TestCalorieCount(unittest.TestCase):


    puzzle_input = ["1000",
                    "2000",
                    "3000",
                    "",
                    "4000",
                    "",
                    "5000",
                    "6000",
                    "",
                    "7000",
                    "8000",
                    "9000",
                    "",
                    "10000",]

    def test_part_one(self):
        expected_result = 24000
        calorie_count = CalorieCount(self.puzzle_input)
        self.assertEqual(calorie_count.most_calories(), expected_result)

    def test_part_two(self):
        expected_result = 45000
        calorie_count = CalorieCount(self.puzzle_input)
        self.assertEqual(calorie_count.sum_top_3_calories(), expected_result)