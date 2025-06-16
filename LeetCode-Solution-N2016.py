# LeetCode problem N2016: Maximum Difference Between Increasing Elements
# difficulty: Easy
from typing import List

class Solution:
    
    # Brute force solution with O(n^2) time complexity
    def maximumDifference(self, nums: List[int]) -> int:
        
        # Step 1: Initialize max_diff to -1
        max_diff = -1
        
        # Step 2: Iterate through the list
        for n in range(len(nums)-1):
            
            # Step 3: Check if the current number is less than the maximum of the remaining numbers
            if max_diff < (max(nums[n+1:]) - nums[n]) and (max(nums[n+1:]) - nums[n]) != 0:
                
                # Step 4: Update max_diff if the condition is met
                max_diff = (max(nums[n+1:]) - nums[n])
                
        # Step 5: Return the maximum difference found
        return max_diff
    
    # Time complexity: O(n^2)
    # Space complexity: O(1)
        
    # Optimized solution with O(n) time complexity
    def maximumDifference2(self, nums: List[int]) -> int:
        
        # Step 1: Initialize ans to -1 and temp_max to the last element of nums
        ans = -1
        temp_max = nums[len(nums)-1]
        
        # Step 2: Iterate through the list in reverse order
        for n in range(len(nums)-2, -1, -1):
            
            # Step 3: Update temp_max if the current number is less than or equal to temp_max
            if nums[n] >= temp_max:
                temp_max = nums[n]
                
            # Step 4: Calculate the maximum difference if the current number is bigger than temp_max
            else:
                ans = max(ans, (temp_max - nums[n]))
                
        # Step 5: Return the maximum difference found
        return ans
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    
nums = [7,1,5,4]
nums2 = [9,4,3,2]
sol = Solution()
print(sol.maximumDifference(nums))  # Output: 4
print(sol.maximumDifference2(nums2))  # Output: -1
