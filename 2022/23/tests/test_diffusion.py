import unittest
from diffusion import Diffusion
class TestDiffusion(unittest.TestCase):

    puzzle_input = ["....#..",
                    "..###.#",
                    "#...#.#",
                    ".#...##",
                    "#.###..",
                    "##.#.##",
                    ".#..#..",]

    def test_part_one(self):
        diffusion = Diffusion(self.puzzle_input)
        expected_result = 110
        self.assertEqual(diffusion.num_ground_tiles(), expected_result)
    
    def test_part_two(self):
        pass