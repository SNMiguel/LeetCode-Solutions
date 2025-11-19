# LeetCode Problem N2154: Keep Multiplying Found Values by Two
# Difficulty: Easy
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            for num in nums:
                if original == num:
                    original = original * 2
        return original
    
# Time Complexity: O(n * m) where n is the number of elements in nums and m is the number of times original is doubled.
# Space Complexity: O(1) as we are using constant extra space.

nums = [5, 3, 6, 1, 12]
original = 3

nums2 = [2, 7, 9]
original2 = 4

solution = Solution()
print(solution.findFinalValue(nums, original))  # Output: 24
print(solution.findFinalValue(nums2, original2))  # Output: 4