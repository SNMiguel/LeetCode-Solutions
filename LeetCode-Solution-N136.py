# LeetCode problem N136: Single Number
# Difficulty: Easy

from collections import Counter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Step 1: Count the occurrences of each number in the list
        dic_nums = Counter(nums)
        
        # Step 2: Iterate through the dictionary to find the number that occurs only once.
        for key, value in  dic_nums.items():
            if value == 1:
                return key
                break