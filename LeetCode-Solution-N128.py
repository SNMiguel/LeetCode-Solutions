# LeetCode Problem N128: Longest Consecutive Sequence
# Difficulty: Medium
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Step 1: Set a condition to check if nums is empty
        if nums:
            
            # Step 2: Sort the list and initialize a counter
            s_nums = sorted(nums)
            counter = 1
            
            # Step 3: Initialize a list to hold the lengths of consecutive sequences
            l_counter = []
             
            # Step 4: Iterate through the sorted list to find consecutive sequences
            for i in range(1, len(nums)):
                
                # Step 5: Check if the current number is consecutive to the previous one
                if s_nums[i] - s_nums[i-1] == 1:
                    counter += 1
                    
                # Step 6: Check if the current number is the same as the previous one
                elif s_nums[i] == s_nums[i-1]:
                    continue
                
                # Step 7: If neither condition is met, append the counter to the list and reset it
                else:
                    l_counter.append(counter)
                    counter = 1
                    
            # Step 8: Append the last counter to the list
            l_counter.append(counter)        
            
            # Step 9: Return the maximum value from the list of counters
            return max(l_counter)
        
        # Step 10: If nums is empty, return 0
        else:
            return 0
        
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing the sorted list and counters
        
nums = [100,4,200,1,3,2]
nums1 = [0,3,7,2,5,8,4,6,0,1]
solution = Solution()
print(solution.longestConsecutive(nums))  # Output: 4
print(solution.longestConsecutive(nums1))  # Output: 5
