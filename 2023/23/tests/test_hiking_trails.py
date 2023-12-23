"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from hiking_trails import HikingTrails
class TestHikingTrails(unittest.TestCase):


    puzzle_input = ["#.#####################",
                    "#.......#########...###",
                    "#######.#########.#.###",
                    "###.....#.>.>.###.#.###",
                    "###v#####.#v#.###.#.###",
                    "###.>...#.#.#.....#...#",
                    "###v###.#.#.#########.#",
                    "###...#.#.#.......#...#",
                    "#####.#.#.#######.#.###",
                    "#.....#.#.#.......#...#",
                    "#.#####.#.#.#########v#",
                    "#.#...#...#...###...>.#",
                    "#.#.#v#######v###.###v#",
                    "#...#.>.#...>.>.#.###.#",
                    "#####v#.#.###v#.#.###.#",
                    "#.....#...#...#.#.#...#",
                    "#.#########.###.#.#.###",
                    "#...###...#...#...#.###",
                    "###.###.#.###v#####v###",
                    "#...#...#.#.>.>.#.>.###",
                    "#.###.###.#.###.#.#v###",
                    "#.....###...###...#...#",
                    "#####################.#",]

    def test_part_one(self):
                        
        hiking_trails = HikingTrails(self.puzzle_input)
        expected_result = 94
        self.assertEqual(hiking_trails.longest_path(), expected_result)

    def test_part_two(self):
           pass 