# LeetCode problem N3304: Find the K-th Character in String Game I
# Difficulty: Easy

class Solution:
    
    # Step 1: Define a method to get the next letter in the alphabet
    def next_letter(self, letter):
        
        # If the letter is 'z', return 'a', otherwise return the next letter in the alphabet
        if letter == "z":
            return "a"
        else:
            return chr(ord(letter)+1)

    def kthCharacter(self, k: int) -> str:
        
        # Step 2: Initialize the word with the first letter 'a'
        word = "a"
        
        # Step 3: Keep adding letters until the length of the word is at least k
        while len(word) < k:
            
            # Step 4: Initialize an empty string to hold the new letters
            add = ""
            
            # Step 5: For each letter in the current word, get the next letter and append it to the new string
            for letter in word:
                add += self.next_letter(letter)
                
            # Step 6: Append the new letters to the word
            word += add
            
        # Step 7: Return the k-th character in the word (1-indexed)
        return word[k-1]
        
k = 5
k1 = 10
solution = Solution()
print(solution.kthCharacter(k))  # Output: 'b'
print(solution.kthCharacter(k1))  # Output: 'c'

# Time Complexity: O(n), where n is the number of characters in the word generated until the k-th character.
# Space Complexity: O(n), where n is the length of the word generated.