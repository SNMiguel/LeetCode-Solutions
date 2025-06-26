class Solution:
    def isPalindromeTwoPointer(self, s: str) -> bool:
        
        # Step 1: Initialize an empty string to hold the filtered characters
        filtered_s = ""
        
        # Step 2: Filter out non-alphanumeric characters and convert to lowercase
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                if letter.isupper():
                    filtered_s += letter.lower()
                else:
                    filtered_s += letter
                    
        # Step 3: Use two pointers to check if the filtered string is a palindrome
        left = 0
        right = len(filtered_s) - 1
        while left < right:
            
            # If characters at the two pointers are not equal, return False
            if filtered_s[left] != filtered_s[right]:
                return False
                break
            left += 1
            right -= 1
        
        # Step 4: If we reach here, it means the string is a palindrome
        return True
    
    # Time Complexity: O(n)
    # Space Complexity: O(n) for the filtered string
    
    def isPalindrome(self, s: str) -> bool:
        
        # Step 1: Initialize an empty string to hold the filtered characters
        filtered_s = ""
        
        # Step 2: Filter out non-alphanumeric characters and convert to lowercase
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                if letter.isupper():
                    filtered_s += letter.lower()
                else:
                    filtered_s += letter
                    
        # Step 3: Check if the filtered string is equal to its reverse    
        return filtered_s == filtered_s[::-1]
    
    # Time Complexity: O(n)
    # Space Complexity: O(n) for the filtered string
    
s = "A man, a plan, a canal: Panama"
s1 = "race a car"
solution = Solution()
print(solution.isPalindromeTwoPointer(s))  # Output: True
print(solution.isPalindrome(s1))  # Output: False