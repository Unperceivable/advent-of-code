import unittest
from rock_pile import RockPile
class TestRockPile(unittest.TestCase):

    puzzle_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
     
    def test_part_one(self):
        rock_pile = RockPile(self.puzzle_input, num_rocks=2022)
        expected_result = 3068
        rock_pile.drop_rocks()
        self.assertEqual(rock_pile.height, expected_result)
    
    def test_part_two(self):
        pass