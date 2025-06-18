# LeetCode Problem N242: Valid Anagram
# Difficulty: Easy
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
s = "anagram", t = "nagaram"
s1 = "rat", t1 = "car"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: True 
print(solution.isAnagram(s1, t1))  # Output: False

# Time Complexity: O(n), where n is the length of the longer string
# Space Complexity: O(1), since the character set is fixed (lowercase English letters)