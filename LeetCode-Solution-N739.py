# LeetCode problem N739: Daily Temperatures
# Difficulty: Medium

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Step 1: Initialize an empty stack to store pairs (temperature, index)
        stk = []
        
        # Step 2: Initialize the result list with all 0s (default: 0 days to wait)
        answers = [0] * len(temperatures)

        # Step 3: Loop through the temperatures with their index
        for i, val in enumerate(temperatures):

            # Step 4: While there is a temperature on the stack and 
            # the current temperature is higher than the one on top of the stack
            while stk and stk[-1][0] < val:
                # Step 4a: Pop the top of the stack (it's cooler than today's temp)
                stk_val, stk_i = stk.pop()
                
                # Step 4b: Calculate how many days it took to find a warmer temp
                answers[stk_i] = i - stk_i

            # Step 5: Push the current temperature and its index onto the stack
            stk.append((val, i))
        
        # Step 6: Return the final list of answers
        return answers

temperatures = [73,74,75,71,69,72,76,73]
temperatures1 = [30,40,50,60]
solution = Solution()
print(solution.dailyTemperatures(temperatures))
print(solution.dailyTemperatures(temperatures1))

# Time Complexity: O(n) - Each temperature is pushed and popped from the stack at most once.
# Space Complexity: O(n) - The stack can store up to n elements in the worst case.