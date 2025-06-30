# LeetCode problem 15: 3Sum
# Difficulty: Medium
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Step 1: Sort the input list
        nums.sort()
        
        # Step 2: Initialize an empty list to store the results
        res = []
        
        # Step 3: Initialize a variable to hold the length of the input list
        n = len(nums)
        
        # Step 4: Iterate through the list with a for loop
        for i in range(n):
            
            # Step 5: Skip the current iteration if the number is equal to the previous number
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 6: Initialize two pointers, left and right
            left, right = i+1, n-1
            
            # Step 7: Use a while loop to find pairs that sum up to the negative of the current number
            while left < right:
                
                # Step 8: Calculate the total of the current number and the two pointers
                total = nums[i] + nums[left] + nums[right]
                
                # Step 9: Compare the total with zero, if total is less than zero, move the left pointer to the right and if total is greater than zero, move the right pointer to the left
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                    
                # Step 10: If total is equal to zero, append the triplet to the result list and move both pointers inward, skipping duplicates
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        # Step 11: Return the result list
        return res
    
nums = [-1,0,1,2,-1,-4]
nums1 = [0,0,0]
nums2 = [0,1,1]
sol = Solution()
print(sol.threeSum(nums))
print(sol.threeSum(nums1))
print(sol.threeSum(nums2))

# Time Complexity: O(n^2)
# Space Complexity: O(1) for the input list, O(n) for the output
                     