# LeetCode Problem N383: Ransom Note
# Difficulty: Easy

from collections import Counter

# Brute Force Solution
class Solution:
    
    # Step 1: Initialize a function to set up a dictionary 
    def setDictionary(self, dic, string):
        for letter in string:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
    
    # Step 2: Check if the ransom note can be constructed from the magazine
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Step 2.1: Create dictionaries for both ransom note and magazine
        d_rans = {}
        d_mag = {}
        self.setDictionary(d_rans, ransomNote)
        self.setDictionary(d_mag, magazine)
        
        # Step 2.2: Compare the dictionaries to determine if the ransom note can be constructed
        for letter in d_rans:
            if letter in d_mag and d_rans[letter] > d_mag[letter]:
                return False
            elif letter not in d_mag:
                return False
            
        # Step 2.3: If all letters in the ransom note can be matched with the magazine, return True
        return True
    
# Time Complexity: O(r + n), where r is the length of the ransom note and n is the length of the magazine string.
# Space Complexity: O(n) for both solutions, where n is the length of the magazine
    
# Optimal Solution
class SolutionOptimal:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Step 1: Use a Counter to count the occurrences of each character in the magazine
        hashmap = Counter(magazine) # TC for Counter is O(n)

        # Step 2: Iterate through the ransom note and check if each character can be matched
        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch]-=1
            else:
                
                # If a character in the ransom note is not available in the magazine, return False
                return False
            
        # Step 3: If all characters in the ransom note can be matched, return True
        return True
    
# Time Complexity: O(r + n), where r is the length of the ransom note and n is the length of the magazine string.
# Space Complexity: O(n) for both solutions, where n is the length of the magazine string.

ransomNote = "a", magazine = "b"
solution = Solution()
print(solution.canConstruct(ransomNote, magazine))  # Output: False

ransomNote = "aa", magazine = "aab"
solution = SolutionOptimal()
print(solution.canConstruct(ransomNote, magazine))  # Output: True