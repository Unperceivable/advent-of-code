import unittest
from passage_pathing import PassagePathing

class TestPassagePathing(unittest.TestCase):

    puzzle_input_a = ["start-A",
                      "start-b",
                      "A-c",
                      "A-b",
                      "b-d",
                      "A-end",
                      "b-end",]
    
    puzzle_input_b = ["dc-end",
                      "HN-start",
                      "start-kj",
                      "dc-start",
                      "dc-HN",
                      "LN-dc",
                      "HN-end",
                      "kj-sa",
                      "kj-HN",
                      "kj-dc",]

    puzzle_input_c = ["fs-end",
                      "he-DX",
                      "fs-he",
                      "start-DX",
                      "pj-DX",
                      "end-zg",
                      "zg-sl",
                      "zg-pj",
                      "pj-he",
                      "RW-he",
                      "fs-DX",
                      "pj-RW",
                      "zg-RW",
                      "start-pj",
                      "he-WI",
                      "zg-he",
                      "pj-fs",
                      "start-RW",]

    def test_part_one(self):
        passage_pathing = PassagePathing(self.puzzle_input_a)
        expected_result =  10
        self.assertEqual(passage_pathing.get_unique_paths(), expected_result)
        
        passage_pathing = PassagePathing(self.puzzle_input_b)
        expected_result =  19
        self.assertEqual(passage_pathing.get_unique_paths(), expected_result)

        passage_pathing = PassagePathing(self.puzzle_input_c)
        expected_result =  226
        self.assertEqual(passage_pathing.get_unique_paths(), expected_result)

    def test_part_two(self):
        pass