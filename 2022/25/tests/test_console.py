import unittest
from console import Console
class TestConsole(unittest.TestCase):

    puzzle_input = ["1=-0-2",
                    "12111",
                    "2=0=",
                    "21",
                    "2=01",
                    "111",
                    "20012",
                    "112",
                    "1=-1=",
                    "1-12",
                    "12",
                    "1=",
                    "122",]

    def test_part_one(self):
        console = Console(self.puzzle_input)
        expected_result = "2=-1=0"
        self.assertEqual(console.sum_snafu_numbers(), expected_result)
    
    def test_part_two(self):
        pass