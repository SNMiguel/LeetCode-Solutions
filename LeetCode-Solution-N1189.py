# LeetCode Problem N1189: Maximum Number of Balloons
# Difficulty: Easy
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # Step 1: Count the occurrences of each character in the input text
        hmap = Counter(text)
        
        # Step 2: Initialize a list to store the minimum occurrences of each character needed for "balloon"
        occurences = []
        
        # Step 3: Check the occurrences of each character in "balloon"
        for letter in "balloon":
            
            # If the character is not in the hashmap or not enough occurrences, return 0
            if letter not in hmap:
                return 0
                break
            
            # If the character is 'l' or 'o', we need to divide the count by 2
            else:
                occurences.append(int(hmap[letter]/"balloon".count(letter)))

        # Step 4: Return the minimum occurrences found
        if not occurences:
            return 0
        else: 
            return min(occurences)
        
text = "nlaebolko"
text1 = "loonbalxballpoon"
solution = Solution()
print(solution.maxNumberOfBalloons(text))  # Output: 1
print(solution.maxNumberOfBalloons(text1))  # Output: 2

# Time Complexity: O(n), where n is the length of the input string text.
# Space Complexity: O(1), since the size of the hashmap is constant (limited to the characters in "balloon").
