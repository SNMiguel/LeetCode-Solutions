# LeetCode problem N682: Baseball Game
# Difficulty: Easy
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        # Step 1: Initialize a stack to keep track of the scores
        stack = []
        
        # Step 2: Iterate through each operation in the operations list
        for index in range(len(operations)):
            if operations[index] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[index] == "D":
                stack.append(stack[-1] * 2)
            elif operations[index] == "C":
                stack.pop()
            else:
                stack.append(int(operations[index]))
                
        # Step 3: Return the sum of the scores in the stack
        return sum(stack)
    
ops = ["5","2","C","D","+"]
ops1 = ["5","-2","4","C","D","9","+","+"]
sol = Solution()
print(sol.calPoints(ops))   # Output: 30
print(sol.calPoints(ops1))  # Output: 27

# Time Complexity: O(n), where n is the number of operations.
# Space Complexity: O(n), for the stack used to store the scores.