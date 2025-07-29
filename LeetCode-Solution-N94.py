# LeetCode problem N94: Binary Tree Inorder Traversal
# Difficulty: Easy

from typing import Optional, List, null

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Step 1: Initialize an empty list to store the inorder traversal
        n_list = []
        
        # Step 2: Define a recursive function to perform inorder traversal
        def inorder(node):
            if node:
                inorder(node.left)
                n_list.append(node.val)
                inorder(node.right)
        
        # Step 3: Call the recursive function starting from the root
        inorder(root)
        
        # Step 4: Return the list containing the inorder traversal
        return n_list
    
root = [1,null,2,3]
root1 = [1,2,3,4,5,null,8,null,null,6,7,9]
solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2]
print(solution.inorderTraversal(root1))  # Output: [4, 2, 6, 7, 5, 1, 3, 8, 9]

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), for the list storing the inorder traversal.