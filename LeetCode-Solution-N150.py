# LeetCode Problem N150: Evaluate Reverse Polish Notation
# Difficulty: Medium

# We'll use a stack and these two functions to evaluate the Reverse Polish Notation (RPN).
from math import ceil, floor 
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Step 1: Initialize an empty stack to hold the operands
        stk = []
        
        # Step 2: Iterate through each token in the input list
        for t in tokens:
            
            # Step 3: If the token is an operator, pop the top two elements from the stack
            if t in "+-*/":
                b, a = stk.pop(), stk.pop()

                # Step 4: Perform the operation based on the operator and push the result back onto the stack
                if t == "+":
                    stk.append(a+b)
                if t == "-":
                    stk.append(a-b)
                if t == "*":
                    stk.append(a*b)
                if t == "/":
                    div = a/b
                    
                # Step 5: Handle division by flooring or ceiling the result based on its sign
                    if div < 0:
                        stk.append(ceil(div))
                    else:
                        stk.append(floor(div))
                        
            # Step 6: If the token is a number, convert it to an integer and push it onto the stack
            else:
                stk.append(int(t))
                
        # Step 7: The final result will be the only element left in the stack
        return stk[0]
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens1 = ["4","13","5","/","+"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 22
print(solution.evalRPN(tokens1))  # Output: 6

# Time Complexity: O(n), where n is the number of tokens in the input list.
# Space Complexity: O(n), where n is the number of tokens in the input list, as we may need to store all tokens in the stack.