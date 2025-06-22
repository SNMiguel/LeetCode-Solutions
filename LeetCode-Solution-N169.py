# LeetCode Problem N169: Majority Element
# Difficulty: Easy
from typing import List
from collections import Counter

class Solution:
    
    # Brute Force Solution
    def majorityElement(self, nums: List[int]) -> int:
        
        # Step 1: Create a dictionary to count occurrences of each element
        Hmap = Counter(nums)
        
        # Step 2: Find the element with the maximum count
        b_value = max(Hmap.values())
        
        # Step 3: Return the key corresponding to the maximum count
        for key, values in Hmap.items():
            if values == b_value:
                return key
                break
    # Time Complexity: O(n) for counting occurrences
    # Space Complexity: O(n) for the Counter dictionary
            
    def majorityElementOpt(self, nums: List[int]) -> int:
        
        # Return the middle element of the sorted list
        # Since the majority element appears more than n/2 times, it will always be at
        return sorted(nums)[len(nums)//2]
    
    # Time Complexity: O(n log n) due to sorting
    # Space Complexity: O(n) for the Counter dictionary
    
nums = [3,2,3]
nums1 = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))  # Output: 3
print(solution.majorityElementOpt(nums1))  # Output: 2