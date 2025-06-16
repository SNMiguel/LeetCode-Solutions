# LeetCode Problem 771: Jewels and Stones
# Difficulty: Easy

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Step 1: Initialize a counter to zero
        count = 0
        
        # Step 2: Iterate through each stone
        for jewel in stones:
            
            # Step 3: Check if the stone is a jewel
            if jewel in jewels:
                
                # If it is, increment the counter
                count += 1
                
        # Step 4: Return the total count of jewels found in stones
        return count