# LeetCode Problem N49: Group Anagrams
# Difficulty: Medium
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Step 1: Create a dictionary to hold sorted strings as keys and lists of anagrams as values
        s_dict = {}
        
        # Step 2: Iterate through each string in the input list
        for index, string in enumerate(strs):
            
            # Step 3: Sort the string to create a key
            s_sort = "".join(sorted(string))
            
            # Step 4: Use the sorted string as a key in the dictionary
            if s_sort not in s_dict:
                s_dict[s_sort] = []
                s_dict[s_sort].append(strs[index])
            else:
                s_dict[s_sort].append(strs[index])
                
        # Step 5: Return the values of the dictionary as a list of lists
        return list(s_dict.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
strs1 = ["a"]
solution = Solution()
print(solution.groupAnagrams(strs))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams(strs1))  # Output: [["a"]]

# Time Complexity: O(n * k log k), where n is the number of strings and k is the maximum length of a string
# Space Complexity: O(n * k), where n is the number of strings and k is
