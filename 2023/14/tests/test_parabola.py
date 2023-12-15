"""Tests for https://adventofcode.com/2023/day/14 Puzzles."""

import unittest
from parabola import Parabola
class TestHotSprings(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = ["O....#....",
                        "O.OO#....#",
                        ".....##...",
                        "OO.#O....O",
                        ".O.....O#.",
                        "O.#..O.#.#",
                        "..O..#O..O",
                        ".......O..",
                        "#....###..",
                        "#OO..#....",]

        expected_result = 136
        
        parabola = Parabola(puzzle_input)
        parabola.shift_north()
        self.assertEqual(parabola.calc_north_load(), expected_result)

    def test_north_shift(self):
        puzzle_input = ["O....#....",
                        "O.OO#....#",
                        ".....##...",
                        "OO.#O....O",
                        ".O.....O#.",
                        "O.#..O.#.#",
                        "..O..#O..O",
                        ".......O..",
                        "#....###..",
                        "#OO..#....",]

        north_shifted_result =["OOOO.#.O..",
                    "OO..#....#",
                    "OO..O##..O",
                    "O..#.OO...",
                    "........#.",
                    "..#....#.#",
                    "..O..#.O.O",
                    "..O.......",
                    "#....###..",
                    "#....#....",]

        parabola = Parabola(puzzle_input)
        parabola.shift_north()
        self.assertEqual(parabola.control_panel, north_shifted_result)

    def test_spin_cycle(self):
        puzzle_input = ["O....#....",
                        "O.OO#....#",
                        ".....##...",
                        "OO.#O....O",
                        ".O.....O#.",
                        "O.#..O.#.#",
                        "..O..#O..O",
                        ".......O..",
                        "#....###..",
                        "#OO..#....",]
        
        parabola = Parabola(puzzle_input)
        
        first_cycle_result = [".....#....",
            "....#...O#",
            "...OO##...",
            ".OO#......",
            ".....OOO#.",
            ".O#...O#.#",
            "....O#....",
            "......OOOO",
            "#...O###..",
            "#..OO#...."]

        parabola.spin_cycle()
        self.assertEqual(parabola.control_panel, first_cycle_result)
        
        second_cycle_result=[".....#....",
            "....#...O#",
            ".....##...",
            "..O#......",
            ".....OOO#.",
            ".O#...O#.#",
            "....O#...O",
            ".......OOO",
            "#..OO###..",
            "#.OOO#...O"]
        
        parabola.spin_cycle()
        self.assertEqual(parabola.control_panel, second_cycle_result)

        third_cycle_result = [".....#....",
            "....#...O#",
            ".....##...",
            "..O#......",
            ".....OOO#.",
            ".O#...O#.#",
            "....O#...O",
            ".......OOO",
            "#...O###.O",
            "#.OOO#...O"]
        
        parabola.spin_cycle()
        self.assertEqual(parabola.control_panel, third_cycle_result)

    def test_part_two(self):
        """."""
        puzzle_input = ["O....#....",
                        "O.OO#....#",
                        ".....##...",
                        "OO.#O....O",
                        ".O.....O#.",
                        "O.#..O.#.#",
                        "..O..#O..O",
                        ".......O..",
                        "#....###..",
                        "#OO..#....",]
        print("!!!!!!!!!!!!LAST TEST !!!!!!!!!!!!")
        parabola = Parabola(puzzle_input)
        parabola.spin_cycle(1000000000)
        expected_result = 64
        self.assertEqual(parabola.calc_north_load(), expected_result)
        