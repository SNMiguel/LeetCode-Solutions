# LeetCode Solution N1768: Merge Strings Alternately
# Difficulty: Easy

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Step 1: Get the minimum length of the words
        min_length = min(len(word1), len(word2))

        # Step 2: Make a variable for merged words
        merged = ""

        # Step 3: Add up and mege the first letters of both words
        for index in range(min_length):
            merged += word1[index]
            merged += word2[index]
        
        # Step 4: Make a variable that holds the longest word
        if len(word1) < len(word2):
            longest = word2
        elif len(word2) < len(word1):
            longest = word1
        else:
            longest = word1

        # Step 5: Returning the merged letters added to the remaining ones of the longest word
        return (merged + longest[min_length:])
    
word1 = "abc"
word2 = "pqr"
word3 = "ab"
word4 = "pqrs"
word5 = "abcd"
word6 = "pq"
sol = Solution()
print(sol.mergeAlternately(word1, word2))  # Output: "apbqcr"
print(sol.mergeAlternately(word3, word4))  # Output: "apbqrs"
print(sol.mergeAlternately(word5, word6))  # Output: "apbqcd"

# Time Complexity: O(n)
# Space Complexity: O(n)