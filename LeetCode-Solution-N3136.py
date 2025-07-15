# LeetCode problem N3136: Valid Word Checker
# Difficulty: Easy

class Solution:
    def isValid(self, word: str) -> bool:
        
        # Step 1: Define consonants and vowels
        cons = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vow = "aeiouAEIOU"
        
        # Step 2: Check if the word contains at least one consonant and one vowel
        c1 = False
        c2 = False
        
        # Step 3: Check the length of the word and iterate through its letters if conditions are met
        if len(word) > 2:
            
            # Step 4: Iterate through each letter in the word
            for letter in word:
                
                # Step 5: Check if the letter is a digit, consonant, or vowel
                if letter.isdigit():
                    continue
                elif letter.isalpha() and letter in cons:
                    c1 = True
                elif letter.isalpha() and letter in vow:
                    c2 = True
                    
                # Step 7: if both conditions are not met, return False
                else:
                    return False
                    break
            
            # Step 8: Return True if both conditions are met
            return c1 and c2
        
        # Step 9: If the word is too short, return False
        else:
            return False
        
word = "234Adas"
word1 = "b3"
word2 = "a3$e"
sol = Solution()
print(sol.isValid(word))   # Output: True
print(sol.isValid(word1))  # Output: False
print(sol.isValid(word2))  # Output: False

# Time Complexity: O(n), where n is the length of the word.
# Space Complexity: O(1), since we are using a constant amount of space for variables.
# Note: The code checks if the word contains at least one consonant and one vowel