# LeetCode Problem 771: Jewels and Stones
# Difficulty: Easy

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Step 0: Convert jewels to a set for O(1) lookups
        filtered_jewels = set(jewels)
        
        # Step 1: Initialize a counter to zero
        count = 0
        
        # Step 2: Iterate through each stone
        for jewel in stones:
            
            # Step 3: Check if the stone is a jewel
            if jewel in filtered_jewels:
                
                # If it is, increment the counter
                count += 1
                
        # Step 4: Return the total count of jewels found in stones
        return count
    
jewels = "aA"
stones = "aAAbbbb"
solution = Solution()
print(solution.numJewelsInStones(jewels, stones))  # Output: 3

# Time complexity: O(n + m), where n is the length of jewels and m is the length of stones.
# Space complexity: O(n), where n is the number of unique jewels.