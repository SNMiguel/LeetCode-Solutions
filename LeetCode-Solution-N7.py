# LeetCode Problem N7: Reverse Integer
# Difficulty: medium

class Solution:
    def reverse(self, x: int) -> int:
        
        # Step 1: Check if x is negative or positive
        if x < 0:
            
            # Step 2: Convert x to string, reverse it, and convert back to int also, check if the reversed integer is within the 32-bit signed integer range
            str_x = str(x*-1)
            return (-1)*(int(str_x[::-1])) if (-1)*(int(str_x[::-1])) in range(-(2)**31, 2**31) else 0
        
        # Step 3: If x is positive, do the same but without the negative sign
        else:
            str_x = str(x)
            return (int(str_x[::-1])) if (int(str_x[::-1])) in range(-(2)**31, 2**31) else 0
        
x = 123
x1 = -123
x2 = 120
sol = Solution()
print(sol.reverse(x))   # Output: 321
print(sol.reverse(x1))  # Output: -321
print(sol.reverse(x2))  # Output: 21

# Time Complexity: O(n), where n is the number of digits in x.
# Space Complexity: O(n), for storing the string representation of x.