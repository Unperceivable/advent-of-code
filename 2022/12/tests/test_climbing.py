import unittest
from climbing import Climbing
class TestClimbing(unittest.TestCase):

    puzzle_input = ["Sabqponm"
                     "abcryxxl"
                     "accszExk"
                     "acctuvwj"
                     "abdefghi"]      

    def test_part_one(self):
        expected_result = 31
        self.assertEqual(Climbing(self.puzzle_input).shortest_path(), expected_result)
