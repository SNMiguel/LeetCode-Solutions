# LeetCode Solution N231: Power of Two
# Difficulty: Easy

import math

# -----------------------------
# Solution 1: Math-based method
# -----------------------------
# NOTE: This works reliably for small numbers, but may fail for very large n
#       due to floating-point precision issues with math.log().
class SolutionMath:
    def isPowerOfTwo(self, n: int) -> bool:
        # Step 1: Ensure n is positive (powers of two are > 0)
        if n <= 0:
            return False
        
        # Step 2: Calculate the base-2 logarithm of n
        log_value = math.log(n, 2)
        
        # Step 3: Check if the log value is an integer (no fractional part)
        # If it is, n is a power of two.
        return log_value == int(log_value)


# ------------------------------
# Solution 2: Bitwise AND method
# ------------------------------
# This works for ALL positive integers without floating-point issues.
class SolutionBitwise:
    def isPowerOfTwo(self, n: int) -> bool:
        # Step 1: Ensure n is positive
        # Step 2: Use the bitwise trick:
        #    - A power of two in binary has exactly one '1' bit.
        #    - Subtracting 1 flips all bits after that '1'.
        #    - n & (n - 1) will be 0 if n is a power of two.
        return n > 0 and (n & (n - 1)) == 0
    
n = 1
n1 = 16
n2 = 3
n3 = 536870912
sol_math = SolutionMath()
sol_bitwise = SolutionBitwise()
print(sol_math.isPowerOfTwo(n))  # Output: True
print(sol_math.isPowerOfTwo(n1))  # Output: True
print(sol_math.isPowerOfTwo(n2))  # Output: False
print(sol_bitwise.isPowerOfTwo(n3))  # Output: True

# Time Complexity: O(log n) for the math-based solution, O(1) for the bitwise solution
# Space Complexity: O(1) for both solutions