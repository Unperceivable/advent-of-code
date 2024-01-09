"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from monkey_business import MonkeyBusiness
class TestMonkeyBusiness(unittest.TestCase):

    puzzle_input = ["Monkey 0:",
                    "  Starting items: 79, 98",
                    "  Operation: new = old * 19",
                    "  Test: divisible by 23",
                    "    If true: throw to monkey 2",
                    "    If false: throw to monkey 3",
                    "",
                    "Monkey 1:",
                    "  Starting items: 54, 65, 75, 74",
                    "  Operation: new = old + 6",
                    "  Test: divisible by 19",
                    "    If true: throw to monkey 2",
                    "    If false: throw to monkey 0",
                    "",
                    "Monkey 2:",
                    "  Starting items: 79, 60, 97",
                    "  Operation: new = old * old",
                    "  Test: divisible by 13",
                    "    If true: throw to monkey 1",
                    "    If false: throw to monkey 3",
                    "",
                    "Monkey 3:",
                    "  Starting items: 74",
                    "  Operation: new = old + 3",
                    "  Test: divisible by 17",
                    "    If true: throw to monkey 0",
                    "    If false: throw to monkey 1]",]
    
    def test_part_one(self):
        monkey_buisness = MonkeyBusiness(self.puzzle_input)
        expected_monkey_business_level = 10605
        self.assertEqual(monkey_buisness.level, expected_monkey_business_level)

    
    def test_part_two(self):
        pass