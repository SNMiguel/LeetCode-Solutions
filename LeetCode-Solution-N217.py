# LeetCode problem 217: Contains Duplicate
# Difficulty: Easy
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Check if the length of the list is not equal to the length of the set created from the list.
        return len(nums) != len(set(nums))
    
nums = [1,2,3,1]
nums1 = [1,2,3,4]
solution = Solution()
print(solution.containsDuplicate(nums))  # Output: True
print(solution.containsDuplicate(nums1))  # Output: False

# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(n), for storing the set of unique elements.