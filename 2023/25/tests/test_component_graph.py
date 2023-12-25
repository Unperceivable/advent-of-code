"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from component_graph import ComponentGraph
class TestComponentGraph(unittest.TestCase):


    puzzle_input = ["jqt: rhn xhk nvd",
                    "rsh: frs pzl lsr",
                    "xhk: hfx",
                    "cmg: qnr nvd lhk bvb",
                    "rhn: xhk bvb hfx",
                    "bvb: xhk hfx",
                    "pzl: lsr hfx nvd",
                    "qnr: nvd",
                    "ntq: jqt hfx bvb xhk",
                    "nvd: lhk",
                    "lsr: lhk",
                    "rzs: qnr cmg lsr rsh",
                    "frs: qnr lhk lsr",]

    def test_part_one(self):
        component_graph = ComponentGraph(self.puzzle_input)
        expected_result = 54
        
        self.assertEqual(component_graph.split_product(), expected_result)

    # def test_part_two(self):
    #     component_graph = ComponentGraph(self.puzzle_input, slippery=False)
    #     expected_result = 154
    #     self.assertEqual(component_graph.get_collisions(), expected_result)