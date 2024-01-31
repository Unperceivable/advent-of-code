import unittest
from whales import Whales

class TestWhales(unittest.TestCase):

    puzzle_input = ["16,1,2,0,4,2,7,1,2,14"]

    def test_part_one(self):
        whales = Whales(self.puzzle_input)
        expected_result = 37
        self.assertEqual(whales.get_fuel_spent(), expected_result)
    
    def test_part_two(self):
        whales = Whales(self.puzzle_input)
        expected_result = 168
        self.assertEqual(whales.get_fuel_spent(escalating_cost=True), expected_result)