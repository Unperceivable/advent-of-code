"""Solutions to https://adventofcode.com/2023/day/6 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path


class CamelCardHand():
    """Hand and Bet for Camel Card Game."""
    def __init__(self, cards: str, bet: str, joker: bool = False):
        self.card_strength = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
        self.cards = cards
        self.bet = int(bet)
        self.joker = joker
        if self.joker:
            self.card_strength.update({"J":1})
        self.base_strength = self.get_hand_str()

    def __ge__(self, other_hand):
        if self.base_strength > other_hand.base_strength:
            return True
        elif self.base_strength == other_hand.base_strength:
            return self.better_card(other_hand.cards)
        else:
            return False
        
    def get_hand_str(self):
        card_str = defaultdict(int)
        for card in self.cards:
            card_str[card] += 1

        if self.joker:
            # get key with the highest value that isnt jokers
            num_jokers = card_str.pop("J", 0)
            if card_str:
                max_key = max(card_str, key=card_str.get)
                card_str[max_key] += num_jokers
            # only jokers
            else:
                card_str["J"] = num_jokers
            
        card_strs = list(card_str.values())
        hand_strs = [val for val in card_strs if val > 1]
        hand_strs.sort(reverse=True)
        if hand_strs:
            hand_str = ".".join([str(val) for val in hand_strs])
            return float(hand_str)
        else:
            return 0
        
    
    def better_card(self, other_cards):
        for my_card, their_card in zip(self.cards, other_cards):    
            if self.card_strength[my_card] > self.card_strength[their_card]:
                return True
            elif self.card_strength[my_card] == self.card_strength[their_card]:
                pass
            else:
                return False

    def __str__(self):
        return f"{self.cards}, {self.base_strength}, {self.bet}"
        
class CamelCardGame():
    def calculate_winnings(camel_cards: "list[str]", joker: bool = False):
        """Returns total winnings for camel card game

        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
        
        
        total winnings = rank * bet: 6440 (765*1 + 220*2 + 28*3 + 684*4 + 483*5)."""

        hand_ranking = []
        for hand in camel_cards:
            hand_rank = 0
            cards, bet = hand.split()
            current_hand = CamelCardHand(cards, bet, joker)
            for hand in hand_ranking:
                if current_hand >= hand:
                    break
                else:
                    hand_rank += 1
                
            hand_ranking.insert(hand_rank, current_hand)
        hand_ranking.reverse()

        total_winings = 0
        for rank, hand in enumerate(hand_ranking, start=1):
            total_winings += rank*hand.bet
        return total_winings
    
if __name__ == "__main__":
    camel_cards_input_path = Path("camel_cards.txt")
    with open(camel_cards_input_path) as camel_cards_file:
        camel_cards_input = camel_cards_file.readlines()
        print(f"Total winnings: {CamelCardGame.calculate_winnings(camel_cards_input)}")
        print(f"Total winnings with jokers: {CamelCardGame.calculate_winnings(camel_cards_input, joker=True)}")