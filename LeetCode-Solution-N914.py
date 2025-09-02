from collections import Counter
from math import gcd
from functools import reduce
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        # Step 1: Count the occurrences of each card in the deck
        h_deck = Counter(deck)
        
        # Step 2: Extract the counts into a list
        deck_c = list(h_deck.values())
        
        # Step 3: Compute the GCD of all counts and check if it's at least 2 or more
        return False if reduce(gcd, deck_c) == 1 else True