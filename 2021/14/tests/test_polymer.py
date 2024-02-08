import unittest
from polymer import Polymer

class TestPolymer(unittest.TestCase):

    puzzle_input = ["NNCB",
                    "",
                    "CH -> B",
                    "HH -> N",
                    "CB -> H",
                    "NH -> C",
                    "HB -> C",
                    "HC -> B",
                    "HN -> C",
                    "NN -> C",
                    "BH -> H",
                    "NC -> B",
                    "NB -> B",
                    "BN -> B",
                    "BB -> N",
                    "BC -> B",
                    "CC -> N",
                    "CN -> C",]

    def test_part_one(self):
        polymer = Polymer(self.puzzle_input)
        expected_result =  1588
        self.assertEqual(polymer.element_difference(), expected_result)

    def test_part_two(self):
        pass