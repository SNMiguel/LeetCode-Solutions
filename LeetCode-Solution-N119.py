from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # Step 1: Handle base cases
        if rowIndex == 0:
            return [1]
        
        # Step 2: Handle the case for rowIndex 1
        elif rowIndex == 1:
            return [1,1]

        # Step 3: Build Pascal's Triangle up to the desired rowIndex
        else:
            
            # Step 3a: Initialize the triangle with the first two rows
            return_l = [[1], [1,1]]
            
            # Step 3b: Iteratively build each row from rowIndex 2 to the desired rowIndex
            for i in range(2, rowIndex + 1):
                l = [1]
                
                # Step 3c: Initialize pointers to sum adjacent elements from the previous row
                left = 0
                right = 1
                
                # Step 3d: Sum adjacent elements from the previous row to form the current row
                while right < len(return_l[i-1]):
                    l.append(return_l[i-1][left] + return_l[i-1][right])
                    left += 1
                    right += 1
                    
                # Step 3e: Append 1 at the end of the current row
                l.append(1)
                
                # Step 3f: Add the current row to the triangle
                return_l.append(l)
                
            # Step 4: Return the desired row
            return return_l[rowIndex]
        
# Example usage:
solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(4))  # Output: [1, 4, 6, 4, 1]