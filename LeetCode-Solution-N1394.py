# LeetCode Problem N1394: Find Lucky Integer in an Array
# Difficulty: Easy

from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # Step 1: Count the occurrences of each number in the array
        dic_arr = Counter(arr)
        
        # Step 2: Initialize the return value to -1
        ret_value = -1
        
        # Step 3: Iterate through the dictionary to find the lucky integer with the highest value
        for key, value in dic_arr.items():
            if key == value and ret_value < value:
                ret_value = value
        
        # Step 4: Return the lucky integer or -1 if none found
        return ret_value
    
arr = [2,2,3,4]
arr1 = [1,2,2,3,3,3]
arr2 = [2,2,2,3,3]
sol = Solution()
print(sol.findLucky(arr))   # Output: 2 
print(sol.findLucky(arr1))  # Output: 3
print(sol.findLucky(arr2))  # Output: -1

# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(n), for storing the count of each element in the array.