"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from step_counter import StepCounter
from collections import namedtuple
class TestStepCounter(unittest.TestCase):


    puzzle_input = ["...........",
                    ".....###.#.",
                    ".###.##..#.",
                    "..#.#...#..",
                    "....#.#....",
                    ".##..S####.",
                    ".##..#...#.",
                    ".......##..",
                    ".##.#.####.",
                    ".##..##.##.",
                    "...........",]

    def test_part_one(self):
                        
        expected_result = 16
        step_counter = StepCounter(self.puzzle_input)
        plots = step_counter.reachable_plots(steps=6)
        self.assertEqual(plots, expected_result)

    def test_part_two(self):
        test_vector = [(6,16),
                (10,50),]
                # (50,1594),
                # (100,6536),
                # (500,167004),
                # (1000,668697),
                # (5000,16733044)]

        step_counter = StepCounter(self.puzzle_input)

        for steps, expected_result in test_vector:
            plots = step_counter.reachable_plots(steps)
            self.assertEqual(plots, expected_result)
            