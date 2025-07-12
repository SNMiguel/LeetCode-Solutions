# LeetCode Problem N319: Bulb Switcher
# Difficulty: Medium

class Solution:
    
    # Brute Force Solution
    # Time Complexity: O(n^2)
    def bulbSwitch(self, n: int) -> int:
        
        # Step 1: Check if n is 0 or 1, return 0 or 1 respectively.
        if  n == 0:
            return 0
        elif n == 1:
            return 1   
        else:
            
            # Step 2: Create a list of size n initialized to 1 (indicating all bulbs are ON).
            list_n = [1] * n
            
            # Step 3: Iterate through the list starting from the second bulb.
            for i in range(1, n):
                
                # For each bulb, toggle the state of every i-th bulb starting from the i-th bulb.
                # If the bulb is ON (1), turn it OFF (0), and if it is OFF (0), turn it ON (1).
                for j in range(i, n, i+1):
                    if list_n[j] == 1:
                        list_n[j] = 0
                    else:
                        list_n[j] = 1

            # Step 4: Count the number of bulbs that are ON (1) and return the sum.
            return sum(list_n)
        
    # Optimized Solution
    # Time Complexity: O(sqrt(n))
    def bulbSwitchOptimized(self, n: int) -> int:
        return int(n**0.5)
    
    # Explanation:
    # Only the perfect square bulbs (like bulb #1, #4, #9, #16, etc.) will remain on at the end.
    # Why?
    
    # - A bulb toggles every time a round number divides it.
    # - Most numbers have pairs of divisors (e.g., 6 → 1×6, 2×3 → toggled even number of times → ends up off)
    # - But perfect squares have an odd number of divisors (like 9 → 1×9, 3×3), so they are toggled an odd number of times → ends up on
    
n = 3
n1 = 0
n2 = 19
n3 = 100000000
solution = Solution()
print(solution.bulbSwitch(n))          # Output: 1
print(solution.bulbSwitch(n1))         # Output: 0
print(solution.bulbSwitch(n2))         # Output: 4
print(solution.bulbSwitchOptimized(n3))         # Output: 10000