import unittest
from lanternfish import Lanternfish
class TestLanternfish(unittest.TestCase):

    puzzle_input = ["3,4,3,1,2"]

    def test_part_one(self):
        lanternfish = Lanternfish(self.puzzle_input)
        expected_result = 5934
        self.assertEqual(lanternfish.get_school_size(days=80), expected_result)
    
    def test_part_two(self):
        pass