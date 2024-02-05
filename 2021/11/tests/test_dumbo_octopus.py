import unittest
from dumbo_octopus import DumboOctopus

class TestDumboOctopus(unittest.TestCase):

    puzzle_input = ["5483143223",
                    "2745854711",
                    "5264556173",
                    "6141336146",
                    "6357385478",
                    "4167524645",
                    "2176841721",
                    "6882881134",
                    "4846848554",
                    "5283751526",] 

    def test_part_one(self):
        dumbo_octopus = DumboOctopus(self.puzzle_input)
        expected_result =  1656
        self.assertEqual(dumbo_octopus.get_total_flashes(steps=100), expected_result)
    
    def test_part_two(self):
        pass