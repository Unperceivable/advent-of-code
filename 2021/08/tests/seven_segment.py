import unittest
from seven_segment import SevenSegment

class TestSevenSegment(unittest.TestCase):

    puzzle_input = ["16,1,2,0,4,2,7,1,2,14"]

    def test_part_one(self):
        seven_segment = SevenSegment(self.puzzle_input)
        expected_result = 37
        self.assertEqual(seven_segment.num_unique_segment_digits(), expected_result)
    
    def test_part_two(self):
        pass