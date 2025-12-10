# LeetCode Problem 151: Reverse Words in a String
# Difficulty: Medium

class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_s =s.split()
        reversed_s = ""
        for word in list_of_s[::-1]:
            reversed_s += " "
            reversed_s += word
        return reversed_s[1:]
    
# Time Complexity: O(n)
# Space Complexity: O(n)

s1 = "the sky is blue"
s2 = "  hello world  "  
solution = Solution()
print(solution.reverseWords(s1))  # Output: "blue is sky the"
print(solution.reverseWords(s2))  # Output: "world hello"