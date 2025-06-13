# LeetCode problem 54: Spiral Matrix
# Difficulty: Medium
from typing import List

class Solution:
    
    # Step 1: Define the methods to traverse the matrix in spiral order
    def goright(self, matrix, l):
        if matrix and any(matrix):
            l.extend(matrix.pop(0))

    def godown(self, matrix, l):
        if matrix and any(matrix):
            for mat in matrix:
                l.append(mat.pop())

    def goleft(self, matrix, l):
        if matrix and any(matrix):
            temp = matrix.pop()
            l.extend(temp[::-1])

    def goup(self, matrix, l):
        if matrix and any(matrix):
            for i in range(len(matrix) - 1, -1, -1):
                l.append(matrix[i].pop(0))

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Step 2: Initialize an empty list to store the result
        l = []
        
        # Step 3: Continue traversing the matrix in spiral order until it's empty
        while matrix and any(matrix):
            self.goright(matrix, l)
            self.godown(matrix, l)
            self.goleft(matrix, l)
            self.goup(matrix, l)
            
        # Step 4: Return the result list
        return l
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix2 = [[7],[9],[6]]
solution = Solution()
print(solution.spiralOrder(matrix))   # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(solution.spiralOrder(matrix1))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(solution.spiralOrder(matrix2))  # Output: [7, 9, 6]

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(m * n) for storing the result in the list.