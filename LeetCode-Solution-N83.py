# LeetCode problem N83: Remove Duplicates from Sorted List
# Difficulty: Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1: Initialize an empty list to keep track of seen values
        c_list = []
        
        # Step 2: Traverse the linked list
        current = head
        if head:
            
            # Step 3: Add the first node's value to the list
            c_list.append(current.val)
            
            # Step 4: Iterate through the linked list
            while current.next:
                
                # Step 5: If the next node's value is already in the list, skip it
                if current.next.val in c_list:
                    current.next = current.next.next
                    
                # Step 6: If the next node's value is not in the list, add it to the list and move to the next node
                else:
                    c_list.append(current.next.val)
                    current = current.next
        
        # Step 7: Return the modified linked list
        return head