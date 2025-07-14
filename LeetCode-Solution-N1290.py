# LeetCode problem N1290: Convert Binary Number in a Linked List to Integer
# Difficulty: Easy

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        # Step 1: Initialize an empty string to build the binary number
        string = ""
        
        # Step 2: Traverse the linked list and append each node's value to the string
        current = head
        while current:
            string += str(current.val)
            current = current.next

        # Step 3: Reverse the string to process it from least significant bit to most significant bit and initialize a value variable
        value = 0
        string = string[::-1]

        # Step 4: Calculate the decimal value by iterating through the string
        for i in range(len(string)):
            value += (int(string[i]) * (2**i))

        # Step 5: Return the calculated decimal value
        return value
    
head = [1,0,1]
head1 = [0]
solution = Solution()
print(solution.getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))  # Output: 5
print(solution.getDecimalValue(ListNode(0)))  # Output: 0

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), for storing the binary string representation.