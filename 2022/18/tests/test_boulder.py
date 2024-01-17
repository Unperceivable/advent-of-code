import unittest
from boulder import Boulder
class TestBoulder(unittest.TestCase):

    puzzle_input = ["2,2,2",
                    "1,2,2",
                    "3,2,2",
                    "2,1,2",
                    "2,3,2",
                    "2,2,1",
                    "2,2,3",
                    "2,2,4",
                    "2,2,6",
                    "1,2,5",
                    "3,2,5",
                    "2,1,5",
                    "2,3,5",]
     
    def test_part_one(self):
        boulder = Boulder(self.puzzle_input)
        expected_result = 64
        self.assertEqual(boulder.lava_droplet(), expected_result)
    
    def test_part_two(self):
        pass