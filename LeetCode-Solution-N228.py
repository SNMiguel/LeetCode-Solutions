# LeetCode Solution N228: Summary Ranges
# Difficulty: Easy
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # Step 1: Initialize an empty list to hold the output and a holder for the range
        output = []
        
        # Step 2: Initialize a holder to track the range
        holder = 0
        
        # Step 3: Handle edge cases for empty or single-element lists
        if len(nums) == 0:
            return output
        elif len(nums) == 1:
            output.append(str(nums[0]))
            return output
        
        # Step 4: Handle the case where the list has more than one element
        else:
            
            # Step 5: Sort the list and append a number to handle the last range
            nums.append(nums[-1] + 2)
            
            # Step 6: Iterate through the list to find ranges
            for i in range(len(nums) - 1):
                
                # Step 7: Initialize a start variable to track the beginning of a range
                start = nums[i]
                
                # Step 8: Check if the next number is not consecutive
                if nums[i + 1] - start != 1 and holder == 0:
                    output.append(str(start))
                    
                # Step 9: Check if the next number is consecutive
                elif nums[i + 1] - start != 1 and holder > 0:
                    output[-1] += ("->" + str(start))
                    holder = 0
                    
                # Step 10: Handle the case where the next number is consecutive
                elif nums[i + 1] - start == 1 and holder == 0:
                    holder += 1
                    output.append(str(start))
                
                # Step 11: Handle the case where the next number is consecutive and holder is already set
                else:
                    holder += 1
                    
            # Step 12: Return the output list containing the summary ranges
            return output
        
nums = [0,1,2,4,5,7]
nums1 = [0,2,3,4,6,8,9]
solution = Solution()
print(solution.summaryRanges(nums))  # Output: ["0->2", "4->5", "7"]
print(solution.summaryRanges(nums1))  # Output: ["0", "2->4", "6", "8->9"]

# Time Complexity: O(n)
# Space Complexity: O(n)