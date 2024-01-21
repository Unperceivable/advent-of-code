import unittest
from monkey_map import MonkeyMap
class TestMonkeyMap(unittest.TestCase):

    puzzle_input = ["        ...#",
                    "        .#..",
                    "        #...",
                    "        ....",
                    "...#.......#",
                    "........#...",
                    "..#....#....",
                    "..........#.",
                    "        ...#....",
                    "        .....#..",
                    "        .#......",
                    "        ......#.",
                    "",
                    "10R5L5R10L4R5L5",]

    def test_part_one(self):
        monkey_map = MonkeyMap(self.puzzle_input)
        expected_result = 6032
        self.assertEqual(monkey_map.get_final_password(), expected_result)
    
    def test_part_two(self):
        pass