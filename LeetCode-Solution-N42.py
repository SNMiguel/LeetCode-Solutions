from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Step 1: Check if the height list is empty
        if not height:
            return 0
        
        # Step 2: Initialize two pointers and their respective maximum heights
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        # Step 3: Initialize the variable to store the total water trapped
        water_trapped = 0
        
        # Step 4: Use a two-pointer approach to calculate the water trapped
        while left < right:
            
            # Step 5: Compare the heights at the two pointers
            if height[left] < height[right]:
                
                # Step 5.1: If the left height is less than the last saved maximum left height, update the stored left maximum
                if height[left] >= left_max:
                    left_max = height[left_max]
                    
                # Step 5.2: If the left height is less than the last saved maximum left height, calculate the water trapped
                else:
                    water_trapped += left_max - height[left]
                    
                # Step 5.3: Move the left pointer to the right
                left += 1
                
            # Step 6: If the right height is less than or equal to the left height
            else:
                
                # Step 6.1: If the right height is greater than or equal to the last saved maximum right height, update the stored right maximum
                if height[right] >= right_max:
                    right_max = height[right_max]
                    
                # Step 6.2: If the right height is less than the last saved maximum right height, calculate the water trapped
                else:
                    water_trapped += right_max - height[right]
                    
                # Step 6.3: Move the right pointer to the left
                right -= 1
        
        # Step 7: Return the total water trapped
        return water_trapped
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height1 = [4,2,0,3,2,5]
sol = Solution()
print(sol.trap(height))
print(sol.trap(height1))

# Time Complexity: O(n), where n is the number of elements in the height list.
# Space Complexity: O(1), as we are using a constant amount of space for pointers and maximum heights.