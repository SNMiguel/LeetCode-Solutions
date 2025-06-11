# LeetCode Solution for Problem 238: Product of Array Except Self
# Difficulty: Medium

from typing import List
import math

class Solution:
    
    # Brute Force Solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Step 1: Initialize an empty list to store the results
        answer = []
        
        # Step 2: Iterate through each element in the input list
        for i in range(len(nums)):
            
            # Step 3: Create a temporary list excluding the current element
            nums_temp = nums[:i] + nums[i+1:]
            
            # Step 4: Calculate the product of the temporary list
            answer.append(math.prod(nums_temp))
            
        # Step 5: Return the final answer list
        return answer
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # Note: This solution is not optimal for large input sizes.
    
    # Optimized Solution
    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        
        # Step 1: Initialize variables for left and right products
        l_mult = 1
        r_mult = 1
        
        # Step 2: Create two arrays to store left and right products
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)
        
        # Step 3: Calculate left and right products in a single pass
        for i in range(len(nums)):
            j = -i-1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
            
        # Step 4: Combine the left and right products to get the final result
        return [l*r for l, r in zip(l_arr, r_arr)]
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
nums = [1,2,3,4]
nums1 = [-1,1,0,-3,3]
solution = Solution()
print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelfOptimized(nums1))  # Output: [0, 0, 9, 0, 0]