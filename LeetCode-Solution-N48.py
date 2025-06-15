# Leetcode Solution for Problem 48: Rotate Image
# Difficulty: Medium
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Step 1: Initialize a variable to hold the size of the matrix
        n = len(matrix)
        
        # Step 2: Perform the rotation by first transposing the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 3: Reverse each row of the transposed matrix
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution = Solution()
solution.rotate(matrix)
print(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]
print(matrix1)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]        
    
# Time complexity: O(n^2) 
# Space complexity: O(1)