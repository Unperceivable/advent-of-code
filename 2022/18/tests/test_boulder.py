import unittest
from boulder import Boulder
class TestBoulder(unittest.TestCase):

    puzzle_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
     
    def test_part_one(self):
        boulder = Boulder(self.puzzle_input)
        expected_result = 64
        self.assertEqual(boulder.lava_droplet(), expected_result)
    
    def test_part_two(self):
        pass