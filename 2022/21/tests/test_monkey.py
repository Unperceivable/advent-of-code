import unittest
from monkey import Monkey
class TestMonkey(unittest.TestCase):

    puzzle_input = ["1",
                    "2",
                    "-3",
                    "3",
                    "-2",
                    "0",
                    "4",]     

    def test_part_one(self):
        monkey = Monkey(self.puzzle_input)
        expected_result = 3
        self.assertEqual(monkey.sum_positions(), expected_result)
    
    def test_part_two(self):
        pass