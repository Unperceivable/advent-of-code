"""Boat Race Tests."""

import unittest
from boat_race import boat_race, kerning_boat_race
class TestBoatRace(unittest.TestCase):
    def test_boat_race(self):
        

        boat_race_input = [
                        "Time:      7  15   30",
                        "Distance:  9  40  200",
                        ]

        self.assertEqual(boat_race(boat_race_input), 288)
    
    def test_kerning_boat_race(self):
        

        boat_race_input = [
                        "Time:      7  15   30",
                        "Distance:  9  40  200",
                        ]

        self.assertEqual(kerning_boat_race(boat_race_input), 71503)