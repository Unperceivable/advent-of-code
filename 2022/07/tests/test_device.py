"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from device import Device
class TestDevice(unittest.TestCase):


    puzzle_input = ["$ cd /",
                     "$ ls",
                     "dir a",
                     "14848514 b.txt",
                     "8504156 c.dat",
                     "dir d",
                     "$ cd a",
                     "$ ls",
                     "dir e",
                     "29116 f",
                     "2557 g",
                     "62596 h.lst",
                     "$ cd e",
                     "$ ls",
                     "584 i",
                     "$ cd ..",
                     "$ cd ..",
                     "$ cd d",
                     "$ ls",
                     "4060174 j",
                     "8033020 d.log",
                     "5626152 d.ext",
                     "7214296 k",]

    def test_part_one(self):
        device = Device(self.puzzle_input)
        expected_result = 95437
        self.assertEqual(device.sum_dir_sizes(), expected_result)

    
    def test_part_two(self):
        device = Device(self.puzzle_input)
        expected_result = 24933642
        self.assertEqual(device.min_dir_size_for_deletion(), expected_result)