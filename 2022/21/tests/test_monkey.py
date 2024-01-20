import unittest
from monkey import Monkey
class TestMonkey(unittest.TestCase):

    puzzle_input = ["root: pppw + sjmn",
                    "dbpl: 5",
                    "cczh: sllz + lgvd",
                    "zczc: 2",
                    "ptdq: humn - dvpt",
                    "dvpt: 3",
                    "lfqf: 4",
                    "humn: 5",
                    "ljgn: 2",
                    "sjmn: drzm * dbpl",
                    "sllz: 4",
                    "pppw: cczh / lfqf",
                    "lgvd: ljgn * ptdq",
                    "drzm: hmdt - zczc",
                    "hmdt: 32",]

    def test_part_one(self):
        monkey = Monkey(self.puzzle_input)
        expected_result = 152
        self.assertEqual(monkey.root_value(), expected_result)
    
    def test_part_two(self):
        pass