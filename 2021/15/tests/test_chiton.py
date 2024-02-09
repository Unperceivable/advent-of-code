import unittest
from chiton import Chiton

class TestChiton(unittest.TestCase):

    puzzle_input = ["1163751742",
                    "1381373672",
                    "2136511328",
                    "3694931569",
                    "7463417111",
                    "1319128137",
                    "1359912421",
                    "3125421639",
                    "1293138521",
                    "2311944581",]

    def test_part_one(self):
        chiton = Chiton(self.puzzle_input)
        expected_result =  40
        self.assertEqual(chiton.get_loweset_total_risk(), expected_result)

    def test_part_two(self):
        pass