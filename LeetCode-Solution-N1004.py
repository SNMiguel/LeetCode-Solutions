# LeetCode problem N1004: Max Consecutive Ones III
# Difficulty: Medium

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Step 1: Initialize an empty list to store lengths of valid subarrays
        n_lis = []
        
        # Step 2: Use two pointers to maintain the window of valid subarrays
        left = 0
        right = 0
        
        # Step 3: Iterate through the array with the right pointer
        while right < len(nums):
            
            # Step 4: Check the current element and adjust the window accordingly
            if nums[right] == 0 and k >= 1:
                k -= 1
                right += 1
            elif nums[right] == 0 and k < 1:
                if nums[left] == 0:
                    k += 1
                n_lis.append(right-left)
                left +=1
            else:
                right += 1
                
        # Step 5: Handle the case when the right pointer reaches the end of the array
        n_lis.append(right-left)
        
        # Step 6: Return the maximum length found
        return max(n_lis)
    
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
nums1 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k1 = 3
solution = Solution()
print(solution.longestOnes(nums, 2))  # Output: 6
print(solution.longestOnes(nums1, 3))  # Output: 10

# Time Complexity: O(n), where n is the length of the input array.
# Space Complexity: O(n), for storing the lengths of valid subarrays.
# Note: The solution uses a sliding window approach to find the maximum length of consecutive ones with at most k flips of zeros to ones.