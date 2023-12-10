"""Tests for https://adventofcode.com/2023/day/8 Puzzles."""

import unittest
from pipe_maze import PipeMaze
class TestPipeMaze(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = [".....",
                        ".S-7.",
                        ".|.|.",
                        ".L-J.",
                        ".....",]
        expected_result = 4
        
        
        self.assertEqual(PipeMaze(puzzle_input).max_dist_from_start(), expected_result)
        
        puzzle_input = ["..F7.",
                        ".FJ|.",
                        "SJ.L7",
                        "|F--J",
                        "LJ...",]
        expected_result = 8

    def test_part_two(self):
        
        puzzle_input = ["...........",
                        ".S-------7.",
                        ".|F-----7|.",
                        ".||.....||.",
                        ".||.....||.",
                        ".|L-7.F-J|.",
                        ".|..|.|..|.",
                        ".L--J.L--J.",
                        "..........."]      
        expected_result = 4
        self.assertEqual(PipeMaze(puzzle_input).num_enclosed_tiles(), expected_result)

        puzzle_input = ["..........",
                        ".S------7.",
                        ".|F----7|.",
                        ".||....||.",
                        ".||....||.",
                        ".|L-7F-J|.",
                        ".|..||..|.",
                        ".L--JL--J.",
                        ".........."]      
        expected_result = 4
        self.assertEqual(PipeMaze(puzzle_input).num_enclosed_tiles(), expected_result)

        puzzle_input = [".F----7F7F7F7F-7....",
                        ".|F--7||||||||FJ....",
                        ".||.FJ||||||||L7....",
                        "FJL7L7LJLJ||LJ.L-7..",
                        "L--J.L7...LJS7F-7L7.",
                        "....F-J..F7FJ|L7L7L7",
                        "....L7.F7||L7|.L7L7|",
                        ".....|FJLJ|FJ|F7|.LJ",
                        "....FJL-7.||.||||...",
                        "....L---J.LJ.LJLJ..."]      
        expected_result = 8
        self.assertEqual(PipeMaze(puzzle_input).num_enclosed_tiles(), expected_result)

        
        puzzle_input = ["FF7FSF7F7F7F7F7F---7",
                        "L|LJ||||||||||||F--J",
                        "FL-7LJLJ||||||LJL-77",
                        "F--JF--7||LJLJ7F7FJ-",
                        "L---JF-JLJ.||-FJLJJ7",
                        "|F|F-JF---7F7-L7L|7|",
                        "|FFJF7L7F-JF7|JL---7",
                        "7-L-JL7||F7|L7F-7F7|",
                        "L.L7LFJ|||||FJL7||LJ",
                        "L7JLJL-JLJLJL--JLJ.L",]      
        expected_result = 10
        self.assertEqual(PipeMaze(puzzle_input).num_enclosed_tiles(), expected_result)
