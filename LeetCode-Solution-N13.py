# LeetCode Solution N13: Roman to Integer
# Difficulty: Easy
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:

        # Step 1: Make a dictionary that holds the value of each letters and their value in integer
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        # Step 2: Make a variable that holds the integer value of the roman number
        value = 0

        # Step 3: Make a variable that will be used when iterating through the string
        i = len(s)-1

        # Step 4: Iterate using a while loop going through the string from right to left
        while i > -1:

            # Step 5: Set a condition for the letter at position zero of the string
            if i != 0:

                # Step 6: Set a condition that compares the (i-1)th value and (i)th value
                if roman[s[i-1]] < roman[s[i]]:
                    value = value - roman[s[i-1]] + roman[s[i]]
                    i -= 1
                else:
                    value += roman[s[i]]
            else:
                value += roman[s[i]]

            # Step 6: Decrement the position holding variable accordingly
            i -= 1

        # Step 7: Return the integer value of the roman number
        return value
    
s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))  # Output: 1994

# Time Complexity: O(n)
# Space Complexity: O(1)