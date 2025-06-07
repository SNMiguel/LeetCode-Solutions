# LeetCode Solution N392: "Is Subsequence"
# Difficulty: Easy

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Step 1: Initialize two pointers that will be used to go through the two strings
        i, j = 0, 0

        # Step 2: Iterate through the two words
        while j < len(t) and i < len(s):

            # Step 3: Set a condition to check if they are subsequent
            if t[j] == s[i]:
                i += 1
            j += 1
        
        # Step 4: Compare and return the pointer that is holding the number of subsequent letters and the length of the original string
        return i == len(s)
    
s = "abc", t = "ahbgdc"
s1 = "axc", t1 = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))  # Output: True
print(sol.isSubsequence(s1, t1))  # Output: False

# Time Complexity: O(n)
# Space Complexity: O(1)