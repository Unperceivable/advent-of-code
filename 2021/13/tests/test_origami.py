import unittest
from origami import Origami

class TestOrigami(unittest.TestCase):

    puzzle_input = ["6,10",
                    "0,14",
                    "9,10",
                    "0,3",
                    "10,4",
                    "4,11",
                    "6,0",
                    "6,12",
                    "4,1",
                    "0,13",
                    "10,12",
                    "3,4",
                    "3,0",
                    "8,4",
                    "1,10",
                    "2,14",
                    "8,10",
                    "9,0",
                    "",
                    "fold along y=7",
                    "fold along x=5",]

    def test_part_one(self):
        origami = Origami(self.puzzle_input)
        expected_result =  17
        self.assertEqual(origami.get_visible_dots(), expected_result)

    def test_part_two(self):
        pass