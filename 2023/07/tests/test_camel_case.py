"""Boat Race Tests."""

import unittest
from camel_cards import CamelCardGame
class TestBoatRace(unittest.TestCase):
    def test_camel_cards(self):
        
        camel_cards_input = ["32T3K 765",
                            "T55J5 684",
                            "KK677 28",
                            "KTJJT 220",
                            "QQQJA 483",]

        self.assertEqual(CamelCardGame.calculate_winnings(camel_cards_input), 6440)
        self.assertEqual(CamelCardGame.calculate_winnings(camel_cards_input, joker=True), 5905)