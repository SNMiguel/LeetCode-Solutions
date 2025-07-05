# LeetCode problem N3: Longest Substring Without Repeating Characters
# Difficulty: Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Step 1: Set a condition to check if the string is empty
        if s:
            
            # Step 2: Initialize a holder to keep track of the current substring
            holder = s[0]
            
            # Step 3: Initialize a list to keep track of the lengths of substrings
            length_ss =[]
            
            # Step 4: Iterate through the string starting from the second character
            for letter in s[1:]:
                
                # Step 5: Check if the letter is the same as the last character in the holder
                if letter == holder[-1]:
                    length_ss.append(len(holder))
                    holder = ""
                    holder += letter
                    
                # Step 6: Check if the letter is the same as the first character in the holder
                elif letter == holder[0]:
                    length_ss.append(len(holder))
                    holder = holder[1:]
                    holder += letter
                    
                # Step 7: Check if the letter is already in the holder
                elif letter in holder:
                    length_ss.append(len(holder))
                    holder = holder[holder.index(letter)+1:]
                    holder +=letter
                    
                # Step 8: If the letter is not in the holder, add it to the holder
                else:
                    holder += letter
            
            # Step 9: Append the length of the last holder to the list
            length_ss.append(len(holder))
            
            # Step 10: Return the maximum length from the list of lengths
            return max(length_ss)
        
        # Step 11: If the string is empty, return 0
        else: 
            return 0

s = "abcabcbb"
s1 = "bbbbb"
s2 = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))   # Output: 3
print(sol.lengthOfLongestSubstring(s1))  # Output: 1
print(sol.lengthOfLongestSubstring(s2))  # Output: 3

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), for the holder string and the length_ss list.