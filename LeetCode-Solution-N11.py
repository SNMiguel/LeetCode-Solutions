# LeetCode problem N11: Container With Most Water
# Difficulty: Medium
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Step 1: Initialize two pointers, one at the start and one at the end of the list and a variable to keep track of the maximum area found so far
        left, right, max_a = 0, len(height)-1, 0
        
        # Step 2: Iterate until the two pointers meet
        while left < right:
            
            # Step 3: Calculate the area formed by the lines at the two pointers
            max_a = max(max_a, (min(height[left], height[right])*(right-left)))
            
            # Step 4: Move the pointer pointing to the shorter line inward
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        # Step 5: Return the maximum area found
        return max_a
    
height = [1,8,6,2,5,4,8,3,7]
height1 = [1,1]
solution = Solution()
print(solution.maxArea(height))  # Output: 49
print(solution.maxArea(height1))  # Output: 1

# Time Complexity: O(n)
# Space Complexity: O(1)