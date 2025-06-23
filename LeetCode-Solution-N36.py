# LeetCode Problem N36: Valid Sudoku
# Difficulty: Medium
from typing import List

# Brute force solution
# There will be no precise optimization for this problem since the board is always 9x9.
class Solution:
    
    # Step 1: Initialize a funcition to check each 3x3 sub-box for duplicates
    def checkbox(self, i, j, board):
        checker = ""
        checker += board[i][j]
        checker += board[i][j+1]
        checker += board[i][j+2]
        checker += board[i+1][j]
        checker += board[i+1][j+1]
        checker += board[i+1][j+2]
        checker += board[i+2][j]
        checker += board[i+2][j+1]
        checker += board[i+2][j+2]
        if len(checker.replace(".", "")) == len(set(checker.replace(".", ""))):
            return 0
        else:
            return 1

    # Step 2: Initialize a function to check each row for duplicates
    def checkrow(self, lst):
        checker = "".join(lst)
        if len(checker.replace(".", "")) == len(set(checker.replace(".", ""))):
            return 0
        else:
            return 1

    # Step 3: Initialize a function to check each column for duplicates
    def checkcolumn(self, i, board):
        checker = ""
        for x in range(9):
            checker += board[x][i]
        if len(checker.replace(".", "")) == len(set(checker.replace(".", ""))):
            return 0
        else:
            return 1

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Step 4: Initiaze a variable to keep track of errors
        error = 0
        
        # Step 5: Check each row and column for duplicates
        for i in range(9):
            error += self.checkrow(board[i])
            error += self.checkcolumn(i, board)
            if error != 0:
                break
        
        # Step 6: Check each 3x3 sub-box for duplicates if there are no errors in rows and columns
        if error != 0:
            return False
        else:
            error += self.checkbox(0, 0, board)
            error += self.checkbox(0, 3, board)
            error += self.checkbox(0, 6, board)
            error += self.checkbox(3, 0, board)
            error += self.checkbox(3, 3, board)
            error += self.checkbox(3, 6, board)
            error += self.checkbox(6, 0, board)
            error += self.checkbox(6, 3, board)
            error += self.checkbox(6, 6, board)
            
            # Step 7: Return True if no errors, otherwise return False
            if error != 0:
                return False
            else:
                return True

# Time Complexity: O(1) - The board is always 9x9, so the time complexity is constant.
# Space Complexity: O(1) - The space used is also constant since we are not

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))  # Expected output: True    
print(sol.isValidSudoku(board2)) # Expected output: False
