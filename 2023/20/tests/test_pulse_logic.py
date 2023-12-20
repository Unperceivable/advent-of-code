"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from pulse_logic import PulseLogic
class TestPulseLogic(unittest.TestCase):

    def test_part_one(self):
        puzzle_input = ["broadcaster -> a, b, c",
                        "%a -> b",
                        "%b -> c",
                        "%c -> inv",
                        "&inv -> a",
        ]
                        
        expected_result = 32000000
        
        pulse_logic = PulseLogic(puzzle_input)
        pulse_count = pulse_logic.pulse_count()
        self.assertEqual(pulse_count, expected_result)

        puzzle_input = ["broadcaster -> a",
                        "%a -> inv, con",
                        "&inv -> b",
                        "%b -> con",
                        "&con -> output",]
    
        expected_result = 11687500
        pulse_logic = PulseLogic(puzzle_input)
        pulse_count = pulse_logic.pulse_count()
        self.assertEqual(pulse_count, expected_result)

    def test_part_two(self):
        pass