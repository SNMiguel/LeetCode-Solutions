# LeetCode Problem N206: Reverse Linked List
# Difficulty: Easy

from typing import Optional, ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1: Initialize pointers
        cur = head
        prev = None
        
        # Step 2: Traverse the list and reverse the links
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Step 3: Return the new head of the reversed list
        return prev
    
head = [1,2,3,4,5]
head1 = [1,2]
sol = Solution()
print(sol.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))  # Expected: 5 -> 4 -> 3 -> 2 -> 1
print(sol.reverseList(ListNode(1, ListNode(2))))  # Expected: 2 -> 1
 
# Time Complexity: O(n)
# Space Complexity: O(1)