#LeetCode Problem N1: Two Sum
# Difficulty: Easy
from typing import List

class Solution:
    
    # Approach 1: Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Step 1: Iterate through each element in the list
        for i, x in enumerate(nums):
            
            # Step 2: Check if the complement (target - x) exists in the list
            if target - x in nums and nums.index(target - x) != i:
                
                # Step 3: Return the indices of the two numbers
                return [i, nums.index(target - x)]
                break
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

    
    # Approach 2: Hash Map
    def twoSumOpt(self, nums: List[int], target: int) -> List[int]:
        
        # Step 1: Create a hash map to store the indices of the numbers
        hashmap = {}
        
        # Step 2: Iterate through the list
        for i, num in enumerate(nums):
            
            # Step 3: Calculate the complement and check if it exists in the hash map
            complement = target - num
            
            # Step 4: If it exists, return the indices
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # Step 5: Otherwise, add the current number and its index to the hash map
            hashmap[num] = i
    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    
nums = [2,7,11,15], target = 13
nums1 = [3,3], target1 = 6
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 2
print(solution.twoSumOpt(nums1, target1))  # Output: [0, 1]
