# LeetCode Problem N344: Reverse String
# Difficulty: Easy
from typing import List

class Solution:
    
    # Brute force approach using two pointers
    def reverseString(self, s: List[str]) -> None:
        
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Step 1: Initialize two pointers, one at the start and one at the end of the list
        l = 0
        r = len(s) - 1
        
        # Step 2: Swap the characters at the two pointers until they meet in the middle
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
    # Time Complexity: O(n), where n is the length of the string
    # Space Complexity: O(1), since we are modifying the list in-place
            
    # Built-in method to reverse the string        
    def reverseStringBuiltIn(self, s: List[str]) -> None:
        
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse()

    # Time Complexity: O(n), where n is the length of the string
    # Space Complexity: O(1), since we are modifying the list in-place
    
s = ["h","e","l","l","o"]
s1 = ["H","a","n","n","a","h"]
solution = Solution()
print(solution.reverseString(s)) # Output: ['o', 'l', 'l', 'e', 'h']
print(solution.reverseStringBuiltIn(s1)) # Output: ['h', 'a', 'n', 'n', 'a', 'H']