# LeetCode problem N118: Pascal's Triangle
# Difficulty: Easy

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Step 1: Handle base cases
        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1], [1,1]]

        # Step 2: Build Pascal's Triangle for numRows > 2
        else:
            
            # Step 2a: Initialize the triangle with the first two rows
            return_l = [[1], [1,1]]
            
            # Step 2b: Construct each subsequent row
            for i in range(2, numRows):
                l = [1]
                
                # Step 2c: Initialize pointers to sum adjacent elements from the previous row
                left = 0
                right = 1
                
                # Step 2d: Sum adjacent elements and build the current row
                while right < len(return_l[i-1]):
                    l.append(return_l[i-1][left] + return_l[i-1][right])
                    left += 1
                    right += 1
                    
                # Step 2e: Append the last element of the current row
                l.append(1)
                
                # Step 2f: Add the current row to the triangle
                return_l.append(l)
                
            # Step 2g: Return the completed Pascal's Triangle
            return return_l
        
# Example usage:
solution = Solution()
numRows = 5
print(solution.generate(numRows)) # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]'
numRows = 1
print(solution.generate(numRows)) # Output: [[1]]