"""Trebuchet Tests."""
import unittest
from trebuchet import trebuchet, improved_trebuchet

class TestTrebuchet(unittest.TestCase):

    def test_trebuchet(self):
        """Trebuchet test, sample data from https://adventofcode.com/2023/day/1."""

        calibration_text = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

        self.assertEqual(trebuchet(calibration_text), 142)

    def test_improved_trebuchet(self):
        """Trebuchet test, sample data from https://adventofcode.com/2023/day/1."""

        calibration_text = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
        self.assertEqual(improved_trebuchet(calibration_text), 281)
if __name__ == "__main__":
    unittest.main()