# LeetCode Problem N35: Search Insert Position
# Difficulty: Easy

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Step 1: Initialize left and right pointers
        left, right = 0, len(nums)-1

        # Step 2: Check if the target is less than or equal to the first element
        if target <= nums[left]:
            return 0
        
        # Step 3: Check if the target is greater than the last element
        elif target > nums[right]:
            return len(nums)
        
        # Step 4: Perform binary search to find the correct position
        else:
            while left <= right:
                left += 1
                right -= 1
                if target <= nums[left]:
                    return left
                elif target > nums[right]:
                    return right+1
                
nums1 = [1,3,5,6], target1 = 5
nums = [1,3,5,6], target = 7
solution = Solution()
print(solution.searchInsert(nums1, target1))  # Output: 2
print(solution.searchInsert(nums, target))    # Output: 4

# Time Complexity: O(log n) - Binary search reduces the search space by half each time.
# Space Complexity: O(1) - Only a few variables are used for pointers.