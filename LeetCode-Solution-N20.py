# LeetCode problem N20: Valid Parentheses
# Difficulty: Easy

class Solution:
    def isValid(self, s: str) -> bool:
        
        # Step 1: Initialize a stack to keep track of opening parentheses
        stack = []
        
        # Step 2: Create a mapping of closing parentheses to their corresponding opening parentheses
        CO = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        # Step 3: Iterate through each character in the string
        for c in s:
            
            # Step 4: If the character is a closing parenthesis, check if it matches the top of the stack
            if c in CO:
                if stack and stack[-1] == CO[c]:
                    stack.pop()
                else:
                    return False
                
            # Step 5: If the character is an opening parenthesis, push it onto the stack
            else:
                stack.append(c)
        
        # Step 6: If the stack is empty, all parentheses were matched; otherwise, return False
        return True if not stack else False
    
s = "()"
s1 = "()[]{}"
s2 = "(]"
s3 = "([])"
sol = Solution()
print(sol.isValid(s))   # Output: True
print(sol.isValid(s1))  # Output: True
print(sol.isValid(s2))  # Output: False
print(sol.isValid(s3))  # Output: True

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), for the stack used to store opening parentheses.