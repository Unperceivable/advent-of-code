"""Boat Race Tests."""

import unittest
from navigate import navigate, renavigate
class TestNavigate(unittest.TestCase):
    def test_navigate(self):
        

        map_input = ["RL",
                    "",
                    "AAA = (BBB, CCC)",
                    "BBB = (DDD, EEE)",
                    "CCC = (ZZZ, GGG)",
                    "DDD = (DDD, DDD)",
                    "EEE = (EEE, EEE)",
                    "GGG = (GGG, GGG)",
                    "ZZZ = (ZZZ, ZZZ)",]

        self.assertEqual(navigate(map_input), 2)

        
        map_input = [
                    "LLR",
                    "",
                    "AAA = (BBB, BBB)",
                    "BBB = (AAA, ZZZ)",
                    "ZZZ = (ZZZ, ZZZ)",   
                    ]
        self.assertEqual(navigate(map_input), 6)

    def test_renavigate(self):
        

        map_input = ["RL",
                    "",
                    "AAA = (BBB, CCC)",
                    "BBB = (DDD, EEE)",
                    "CCC = (ZZZ, GGG)",
                    "DDD = (DDD, DDD)",
                    "EEE = (EEE, EEE)",
                    "GGG = (GGG, GGG)",
                    "ZZZ = (ZZZ, ZZZ)",]

        self.assertEqual(navigate(map_input), 2)

        
        map_input = ["LR",
                    "",
                    "11A = (11B, XXX)",
                    "11B = (XXX, 11Z)",
                    "11Z = (11B, XXX)",
                    "22A = (22B, XXX)",
                    "22B = (22C, 22C)",
                    "22C = (22Z, 22Z)",
                    "22Z = (22B, 22B)",
                    "XXX = (XXX, XXX)",]
        self.assertEqual(renavigate(map_input), 6)