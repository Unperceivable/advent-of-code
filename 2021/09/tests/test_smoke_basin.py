import unittest
from smoke_basin import SmokeBasin

class TestSmokeBasin(unittest.TestCase):

    puzzle_input = ["2199943210",
                    "3987894921",
                    "9856789892",
                    "8767896789",
                    "9899965678",] 

    def test_part_one(self):
        smoke_basin = SmokeBasin(self.puzzle_input)
        expected_result = 15
        self.assertEqual(smoke_basin.get_risk_level(), expected_result)
    
    def test_part_two(self):
        pass