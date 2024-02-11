import unittest
from trick_shot import TrickShot

class TestTrickShot(unittest.TestCase):

    puzzle_input = "target area: x=20..30, y=-10..-5"
    
    def test_part_one(self):
        trick_shot = TrickShot(self.puzzle_input)
        expected_result =  45
        self.assertEqual(trick_shot.get_highest_pos(), expected_result)

    def test_part_two(self):
        pass