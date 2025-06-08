# LeetCode Solution N122: Best Time to Buy and Sell Stock II
# Difficulty: Medium

# Brute Force Solution
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Step 1: Initialize two variables that will be holding the best day to buy and best day to sell 
        buy = prices[0]
        sell = prices[0]

        # Step 2: Initialize a variable to hold the profit
        profit = 0

        # Step 3: Iterate through the list of prices
        for i in range(len(prices)):

            # Step 4: Set a condition for when the last element isn't a better day to sell
            if i == (len(prices) - 1) and sell > prices[i]:
                profit += (sell - buy)

            # Step 5: Set a condition for when the last element is the best day to sell
            elif i == (len(prices) - 1) and sell <= prices[i]:
                sell = prices[i]
                profit += (sell - buy)

            # Step 6: Set a condition to sell
            elif prices[i] < sell:
                profit += (sell - buy)
                buy = prices[i]
                sell = prices[i]

            # Step 7: Set a condition to change to a better buy time
            elif prices[i] < buy:
                buy = prices[i]
                sell = prices[i]

            # Step 8: Set a condition to change to a better sell time
            elif prices[i] > sell:
                sell = prices[i]

        # Step 9: Return the profit
        return profit
    
prices = [7,1,5,3,6,4]
prices1 = [7,6,4,3,1]
prices2 = [1,2,3,4,5]
solution = Solution()
print(solution.maxProfit(prices))  # Output: 7
print(solution.maxProfit(prices1)) # Output: 0
print(solution.maxProfit(prices2))  # Output: 4

# Time Complexity: O(n)
# Space Complexity: O(1)

# Optimized Solution

