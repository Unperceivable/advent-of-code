"""Boat Race Tests."""

import unittest
from camel_cards import camel_cards
class TestBoatRace(unittest.TestCase):
    def test_camel_cards(self):
        

        camel_cards_input = ["32T3K 765",
                            "T55J5 684",
                            "KK677 28",
                            "KTJJT 220",
                            "QQQJA 483",]

        self.assertEqual(camel_cards(camel_cards_input), 6440)