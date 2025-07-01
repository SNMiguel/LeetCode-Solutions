# LeetCode problem N3330: Count Possible Strings
# Difficulty: Easy

class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        #  Step 1: Initialize a variable to count the number of possible strings and set it to 1 for the original word
        result = 1
        
        # Step 2: Iterate through the word starting from the second character
        for i in range(1, len(word)):
            
            # Step 3: If the current character is the same as the previous one, increment the count
            if word[i] == word[i-1]:
                result += 1
                
        # Step 4: Return the total count of possible words
        return result
    
word = "abbcccc"
word1 = "aaaa"
word2 = "abcd"
solution = Solution()
print(solution.possibleStringCount(word))   # Output: 5
print(solution.possibleStringCount(word1))  # Output: 4
print(solution.possibleStringCount(word2))  # Output: 1

# Time Complexity: O(n), where n is the length of the word
# Space Complexity: O(1), as we are using a constant amount of space for the result variable