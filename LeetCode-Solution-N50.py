# LeetCode Solution N50: Pow(x, n)
# Difficulty: Medium

def myPow(self, x: float, n: int) -> float:
    
    # Step 1: Define a helper function `f` that computes x^n for positive n
    def f(x, n):
        # Step 1.1: Handle edge case where x is 0
        if x == 0:
            return 0

        # Step 1.2: Base case: any number to the power of 0 is 1
        if n == 0:
            return 1

        # Step 1.3: Recursively compute x^(n//2)
        ans = f(x, n // 2)

        # Step 1.4: Square the result to get x^n (if n is even)
        ans *= ans

        # Step 1.5: If n is odd, multiply by x one more time
        if n % 2 == 1:
            return ans * x
        
        # Step 1.6: If n is even, return the squared result
        return ans

    # Step 2: Handle negative powers by calling `f` with absolute value of n
    ans = f(x, abs(n))

    # Step 3: If the original power was negative, return the reciprocal
    if n < 0:
        return 1 / ans

    # Step 4: Otherwise, return the computed power
    return ans

x = 2.00000, n = 10
x1 = 2.10000, n1 = 3
x2 = 2.00000, n2 = -2
print(myPow(x, n))  # Output: 1024.00000
print(myPow(x1, n1))  # Output: 9.26100
print(myPow(x2, n2))  # Output: 0.25000

# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion stack