# LeetCode problem N1365: How Many Numbers Are Smaller Than the Current Number
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # Step 1: Sort the array and store the sorted version
        tmp = sorted(nums)
        
        # Step 2: Create a dictionary to map each number to its first occurrence index in the sorted array
        dict = {}
        
        # Step 3: Populate the dictionary
        for i,n in enumerate(tmp):
            if n not in dict:
                dict[n] = i
                
        # Step 4: Construct the result using the dictionary
        res = []
        for i in nums:
            res.append(dict[i])
            
        # Step 5: Return the result
        return res
    
nums = [8,1,2,2,3]
nums1 = [6,5,4,8]
print(Solution().smallerNumbersThanCurrent(nums)) # Output: [4,0,1,1,3]
print(Solution().smallerNumbersThanCurrent(nums1)) # Output: [2,1,0,3]

# TIME COMPLEXITY: O(n log n) where n is the length of nums due to the sorting step.
# SPACE COMPLEXITY: O(n) for storing the sorted array and the dictionary.