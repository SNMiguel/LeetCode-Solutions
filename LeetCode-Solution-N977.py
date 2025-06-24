# LeetCode problem N977: Squares of a Sorted Array
# Difficulty: Easy
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Square each number in the array and return a sorted array of those squares.
        return sorted([(x*x) for x in nums])
    
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the new list of squares

nums = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]
sol = Solution()
print(sol.sortedSquares(nums))   # Output: [0, 1, 9, 16, 100]
print(sol.sortedSquares(nums2))  # Output: [4, 9, 9, 49, 121]