import unittest
from boulder import Boulder
class TestBoulder(unittest.TestCase):

    puzzle_input_a = ["1,1,1",
                      "2,1,1"]
    
    puzzle_input_b = ["2,2,2",
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
        boulder = Boulder(self.puzzle_input_a)
        expected_result = 10
        self.assertEqual(boulder.get_lava_drop_surface(), expected_result)

        boulder = Boulder(self.puzzle_input_b)
        expected_result = 64
        self.assertEqual(boulder.get_lava_drop_surface(), expected_result)
    
    def test_part_two(self):
        pass