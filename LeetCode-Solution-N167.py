# LeetCode problem N167: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
from typing import List

class Solution:
    
    # Method 1: Hash Map
    def twoSumHashM(self, numbers: List[int], target: int) -> List[int]:
        
        # Step 1: Create a hash map to store the indices of the numbers
        HashM = {}
        
        # Step 2: Iterate through the list of numbers in reverse order
        for index, value in enumerate(numbers[::-1]):
            
            # Step 3: Calculate the complement of the current number
            n2 = target - value
            
            # Step 4: Check if the complement exists in the hash map
            if n2 in HashM:
                
                # If it does, return the indices of the two numbers
                return [len(numbers)-index, HashM[n2]]
            
            # Step 5: If not, add the current number and its index to the hash map
            HashM[value] = len(numbers)-index
            
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    # Method 2: Two Pointer Technique
    def twoSumTwoP(self, numbers: List[int], target: int) -> List[int]:
        
        # Step 1: Initialize two pointers, one at the start and one at the end of the list
        left = 0
        right = len(numbers) - 1
        
        # Step 2: Iterate until the two pointers meet
        while left < right:
            
            # Step 3: Calculate the sum of the numbers at the two pointers
            total = numbers[left] + numbers[right]
            
            # Step 4: Compare the sum with the target
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                
                # If the sum equals the target, return the indices of the two numbers
                return [left+1, right+1] 
            
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
numbers = [2,7,11,15], target = 9
numbers1 = [2,3,4], target1 = 6
solution = Solution()
print(solution.twoSumHashM(numbers, target))  # Output: [1, 2]
print(solution.twoSumTwoP(numbers1, target1))  # Output: [1, 3]