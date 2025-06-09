# LeetCode Solution N14: Longest Common Prefix
# Difficulty: Easy

# Brute Force Solution
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Step 1: Initialize one variable that will be holding the common prefix and a second one to hold the smallest element of the list 
        prefix = ""
        smallest = min(strs, key=len)
        
        # Step 2: Initialize a variable that will be used to check if there is a difference between prefixes
        different = 0
        
        # Step 3: Iterate through the list to check all letters of the strings from left to right
        for i in range(len(smallest)):

            # Step 4: Initialize a second loop that will be used to go from one string to another
            for j in range(len(strs)):

                # Step 5: Set a condition to confirm a letter is part of the common prefix
                if strs[j][i] == smallest[i] and j == len(strs) - 1 and different == 0:
                    prefix += smallest[i]
                
                # Step 6: Set a condition for when a letter is not part of the common prefix
                elif strs[j][i] != smallest[i]:
                    different +=1

                # Step 7: Set a condition to break the loop the moment there is a difference
                elif different != 0:
                    break

            # Step 8: Set a second condition to break the other loop when a another difference is noticed
            if different != 0:
                break

        # Step 9: Return the common prefix
        return prefix
    
strs = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]
strs2 = ["cir","car"]
strs3 = ["aa","aa"]
strs4 = ["aa","ab"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Output: "fl"
print(solution.longestCommonPrefix(strs1))  # Output: ""
print(solution.longestCommonPrefix(strs2))  # Output: "c"
print(solution.longestCommonPrefix(strs3))  # Output: "aa"
print(solution.longestCommonPrefix(strs4))  # Output: "a"

# Time Complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.
# Space Complexity: O(1), since we are using a constant amount of space for the prefix and other variables.

# Optimized Solution
class SolutionOptimized:
    def longestCommonPrefix(self, word: List[str]) -> str:
        
        # Step 1: Initialize a variable that will be holding the common prefix
        prefix = ""
        
        # Step 2: Sort the list of strings
        word = sorted(word)
        
        # Step 3: Compare the first and last strings in the sorted list to find the common prefix
        first=word[0]
        last=word[-1]
        
        # Step 4: Iterate through the characters of the first and last strings to find the common prefix
        for i in range(min(len(first),len(last))):
            
            # Step 5: If characters at the same position are different, return the prefix
            if(first[i]!=last[i]):
                return prefix
            
            # Step 6: If characters are the same, append to the prefix
            prefix+=first[i]
            
        # Step 7: Return the prefix
        return prefix 
    
# Time Complexity: O(n * log n + m), where n is the number of strings and m is the length of the shortest string.
# Space Complexity: O(1), since we are using a constant amount of space for the prefix and other variables.