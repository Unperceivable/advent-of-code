import unittest
from grove import Grove
class TestGrove(unittest.TestCase):

    puzzle_input = ["1",
                    "2",
                    "-3",
                    "3",
                    "-2",
                    "0",
                    "4",]     

    def test_part_one(self):
        grove = Grove(self.puzzle_input)
        expected_result = 3
        self.assertEqual(grove.sum_positions(), expected_result)
    
    def test_part_two(self):
        pass