import unittest
from minerals import Minerals
class TestMinerals(unittest.TestCase):

    puzzle_input = ["Blueprint 1:",
                    "  Each ore robot costs 4 ore.",
                    "  Each clay robot costs 2 ore.",
                    "  Each obsidian robot costs 3 ore and 14 clay.",
                    "  Each geode robot costs 2 ore and 7 obsidian.",
                    "",
                    "Blueprint 2:",
                    "  Each ore robot costs 2 ore.",
                    "  Each clay robot costs 3 ore.",
                    "  Each obsidian robot costs 3 ore and 8 clay.",
                    "  Each geode robot costs 3 ore and 12 obsidian.",]
     
    def test_part_one(self):
        minerals = Minerals(self.puzzle_input_a)
        expected_result = 33
        self.assertEqual(minerals.quality_level(), expected_result)
    
    def test_part_two(self):
        pass