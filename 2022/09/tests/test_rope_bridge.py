"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from rope_bridge import RopeBridge
class TestRopeBridge(unittest.TestCase):

    puzzle_input_a = ["R 4",
                        "U 4",
                        "L 3",
                        "D 1",
                        "R 4",
                        "D 1",
                        "L 5",
                        "R 2",]
    puzzle_input_b = ["R 5",
                    "U 8",
                    "L 8",
                    "D 3",
                    "R 17",
                    "D 10",
                    "L 25",
                    "U 20",]
    
    def test_part_one(self):
        rope_bridge = RopeBridge(self.puzzle_input_a)
        expected_result = 13
        rope_bridge.move_rope()
        poses = rope_bridge.tail_poses
        num_poses = len(poses)
        self.assertEqual(num_poses, expected_result)

    
    def test_part_two(self):
        rope_bridge = RopeBridge(self.puzzle_input_a, tail_length=9)
        expected_result = 1
        rope_bridge.move_rope()
        poses = rope_bridge.tail_poses
        num_poses = len(poses)
        self.assertEqual(num_poses, expected_result)

        rope_bridge = RopeBridge(self.puzzle_input_b, tail_length=9)
        expected_result = 36
        rope_bridge.move_rope()
        poses = rope_bridge.tail_poses
        num_poses = len(poses)
        self.assertEqual(num_poses, expected_result)