"""Tests for https://adventofcode.com/2023/day/15 Puzzles."""

import unittest
from lens_library import LensLibrary
class TestLensLibrary(unittest.TestCase):

    def test_part_one(self):
        """."""
        puzzle_input = ["HASH"]
        expected_result = 52
        lens_library = LensLibrary(puzzle_input)
        self.assertEqual(lens_library.sum_of_lens_libraryes(), expected_result)

        puzzle_input = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]
        expected_result = 1320
        lens_library = LensLibrary(puzzle_input)
        self.assertEqual(lens_library.sum_of_lens_libraryes(), expected_result)

    def test_part_two(self):
        """."""
        puzzle_input = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]
        expected_result = 145
        lens_library = LensLibrary(puzzle_input)
        self.assertEqual(lens_library.calc_focusing_power(), expected_result)