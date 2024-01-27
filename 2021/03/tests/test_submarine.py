import unittest
from submarine import Submarine
class TestSubmarine(unittest.TestCase):

    puzzle_input = ["00100",
                    "11110",
                    "10110",
                    "10111",
                    "10101",
                    "01111",
                    "00111",
                    "11100",
                    "10000",
                    "11001",
                    "00010",
                    "01010",]

    def test_part_one(self):
        submarine = Submarine(self.puzzle_input)
        expected_result = 198
        self.assertEqual(submarine.get_power_consumption(), expected_result)
    
    def test_part_two(self):
        pass