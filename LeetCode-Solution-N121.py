# LeetCode Solution N121: Best Time to Buy and Sell Stock
# Difficulty: Easy
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Step 1: Initialize two variables that will be holding the best day to buy and best day to sell 
        small = prices[0]
        big = prices[0]

        # Step 2: Initialize a variable to hold the biggest profit
        great = 0

        # Step 3: Iterate through the list of prices
        for i in prices:

            # Step 4: Set a condition for when prices[i] is a better day to buy
            if i < small:
                small = i
                big = i

            # Step 5: Set a condition for when prices[i] is a better day to sell
            elif i > big:
                big = i

                # Step 6: Set a condition that changes the variable that is holding the greatest profit
                if ((big - small) > great):
                    great = big - small

        # Step 7: Return the greatest profit
        return great
    
prices = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
sol = Solution()
print(sol.maxProfit(prices))  # Output: 5
print(sol.maxProfit(prices2))  # Output: 0

# Time Complexity: O(n)
# Space Complexity: O(1)