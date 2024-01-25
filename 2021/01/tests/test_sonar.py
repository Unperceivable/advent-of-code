import unittest
from sonar import Sonar
class TestSonar(unittest.TestCase):

    puzzle_input = ["199",
                    "200",
                    "208",
                    "210",
                    "200",
                    "207",
                    "240",
                    "269",
                    "260",
                    "263",]


    def test_part_one(self):
        sonar = Sonar(self.puzzle_input)
        expected_result = 7
        self.assertEqual(sonar.count_larger_than_prev_value, expected_result)
    
    def test_part_two(self):
        pass