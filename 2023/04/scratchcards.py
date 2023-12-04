
"""Solutions to https://adventofcode.com/2023/day/4 Puzzles."""

import re
from collections import namedtuple, defaultdict
from pathlib import Path

scratchcard_pattern = re.compile(r".*?(\d+):\s*([^|]*)\s*\|\s*(.*)")

def scratchcards(scratchcards: list[str]):
    """Calculate the number of points
    
    example scratchcards:
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    
    For each number in the scratched values (left) that appear in the winning values you get 2^(number of cards -1) points."""
    
    sum_of_points = 0
    for line in scratchcards:
        card_vals = scratchcard_pattern.search(line)
        scratched_vals = set([int(val) for val in card_vals.group(2).split(" ") if val]) 
        winning_vals = set([int(val) for val in card_vals.group(3).split(" ") if val])
    
        wins = len(scratched_vals.intersection(winning_vals))
        if wins:
            sum_of_points += 2**(wins -1)
    return sum_of_points
        

def generative_scratchcards(scratchcards: list[str]):
    """Calculate total number of scratchcards, given winning cards generate more cards
    
    example scratchcards:
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    
    The number ofc N wins in scratchcard in Card X, results in you receiving a duplicate cards of X+1 to X+N."""
    
    # Initialize a defaultdict with the number of cards and a default value of 1
    card_multipliers = defaultdict(lambda: 1, {i: 1 for i in range(1, len(scratchcards) + 1)})
    for line in scratchcards:
        card_vals = scratchcard_pattern.search(line)
        card_number = int(card_vals.group(1))
        scratched_vals = set([int(val) for val in card_vals.group(2).split(" ") if val]) 
        winning_vals = set([int(val) for val in card_vals.group(3).split(" ") if val]) 
        wins = len(scratched_vals.intersection(winning_vals))
        
        for next_card in range(1, wins + 1):
            card_multipliers[card_number+next_card] += card_multipliers[card_number]
    sum_of_cards = sum(list(card_multipliers.values()))
    return sum_of_cards
if __name__ == "__main__":
    scratchcard_input_path = Path("scratchcards.txt")
    with open(scratchcard_input_path) as scratchcard_file:

        scratchcard_input = scratchcard_file.readlines()
        print(f"Scratchcard Points: {scratchcards(scratchcard_input)}")
        print(f"Number of Total Scratchcard: {generative_scratchcards(scratchcard_input)}")