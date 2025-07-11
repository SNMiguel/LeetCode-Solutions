# LeetCode Problem N2: Add Two Numbers
# Difficulty: Medium

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1: Initialize two empty strings to hold the numbers represented by the linked lists.
        str1 = ""
        str2 = ""
        
        # Step 2: Traverse the first linked list and build the string representation of the number.
        current = l1
        while current:
            str1 += str(current.val)
            current = current.next

        # Step 3: Traverse the second linked list and build the string representation of the number.
        current = l2
        while current:
            str2 += str(current.val)
            current = current.next
            
        # Step 4: Initialize a new string to hold the result of the addition and reverse it.
        str3 = str(int(str1[::-1]) + int(str2[::-1]))
        str3 = str3[::-1]
        
        # Step 5: Create a new linked list to hold the result.
        l3 = ListNode(0)
                
        # Step 6: Traverse the result string and build the linked list .
        current = l3
        for digit in str3[:-1]:
            current.val = int(digit)
            current.next = ListNode(0)
            current = current.next
        current.val = int(str3[-1])
        
        # Step 7: Return the head of the new linked list.
        return l3
    
l1 = [2,4,3], l2 = [5,6,4]
l3 = [9,9,9,9,9,9,9], l4 = [9,9,9,9]
l5 = [0], l6 = [0]

sol = Solution()
print(sol.addTwoNumbers(ListNode(*l1), ListNode(*l2)))  # Output: 7 -> 0 -> 8
print(sol.addTwoNumbers(ListNode(*l3), ListNode(*l4)))  # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
print(sol.addTwoNumbers(ListNode(*l5), ListNode(*l6)))  # Output: 0

# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
# Space Complexity: O(n + m), for storing the string representations of the numbers.
