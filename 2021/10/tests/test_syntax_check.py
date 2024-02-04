import unittest
from syntax_check import SyntaxCheck

class TestSyntaxCheck(unittest.TestCase):

    puzzle_input = ["[({(<(())[]>[[{[]{<()<>>",
                    "[(()[<>])]({[<{<<[]>>(",
                    "{([(<{}[<>[]}>{[]{[(<()>",
                    "(((({<>}<{<{<>}{[]{[]{}",
                    "[[<[([]))<([[{}[[()]]]",
                    "[{[{({}]{}}([{[{{{}}([]",
                    "{<[[]]>}<{[{[{[]{()[[[]",
                    "[<(<(<(<{}))><([]([]()",
                    "<{([([[(<>()){}]>(<<{{",
                    "<{([{{}}[<[[[<>{}]]]>[]]",] 

    def test_part_one(self):
        syntax_check = SyntaxCheck(self.puzzle_input)
        expected_result = 26397
        self.assertEqual(syntax_check.get_risk_level(), expected_result)
    
    def test_part_two(self):
        pass