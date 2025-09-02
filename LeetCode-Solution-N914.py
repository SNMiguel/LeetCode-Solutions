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
    
deck = [1,2,3,4,4,3,2,1]
deck1 = [1,1,1,2,2,2,3,3]
print(Solution().hasGroupsSizeX(deck))  # Expected output: True
print(Solution().hasGroupsSizeX(deck1)) # Expected output: False
    
# Time Complexity: O(N) where N is the number of cards in the deck
# Space Complexity: O(N) in the worst case where all cards are unique