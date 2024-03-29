import unittest
from vents import Vents
class TestVents(unittest.TestCase):

    puzzle_input = ["0,9 -> 5,9",
                    "8,0 -> 0,8",
                    "9,4 -> 3,4",
                    "2,2 -> 2,1",
                    "7,0 -> 7,4",
                    "6,4 -> 2,0",
                    "0,9 -> 2,9",
                    "3,4 -> 1,4",
                    "0,0 -> 8,8",
                    "5,5 -> 8,2",]

    def test_part_one(self):
        vents = Vents(self.puzzle_input)
        expected_result = 5
        self.assertEqual(vents.num_overlapping_lines(), expected_result)
    
    def test_part_two(self):
        vents = Vents(self.puzzle_input)
        expected_result = 12
        self.assertEqual(vents.num_overlapping_lines(diagonal_lines=True), expected_result)