"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from sand_slabs import SandSlabs, Brick, Coord
from collections import namedtuple
class TestSandSlabs(unittest.TestCase):


    puzzle_input = ["1,0,1~1,2,1",
                    "0,0,2~2,0,2",
                    "0,2,3~2,2,3",
                    "0,0,4~0,2,4",
                    "2,0,5~2,2,5",
                    "0,1,6~2,1,6",
                    "1,1,8~1,1,9",]

    def test_part_one(self):
                        
        expected_result = 5
        # Set up the 3D array
        sand_slabs = SandSlabs(self.puzzle_input)

        # Define bricks
        brick1 = Brick(Coord(1, 1, 5), Coord(4, 4, 6))
        brick2 = Brick(Coord(6, 6, 5), Coord(8, 8, 7))


        # Visualize the 3D array with bricks
        # sand_slabs.visualize_3d_array()
        # self.assertEqual(0, expected_result)

    def test_part_two(self):
           pass 