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
        self.assertEqual(syntax_check.get_error_score(), expected_result)
    
    def test_part_two(self):
        syntax_check = SyntaxCheck(self.puzzle_input)
        expected_result = 288957
        self.assertEqual(syntax_check.get_completion_score(), expected_result)