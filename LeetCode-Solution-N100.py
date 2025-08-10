# LeetCode Problem N100: Same Tree
# Difficulty: Easy

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' | None = None, right: 'TreeNode' | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # (step 0:) Define a recursive helper function to compare two nodes.
        def checker(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            # (step 1:) If both nodes are None, the current branches match.
            if not p and not q:
                return True
            
            # (step 2:) If exactly one is None, trees differ.
            if not p or not q:
                return False
            
            # (step 3:) If node values differ, trees differ.
            if p.val != q.val:
                return False
            
            # (step 4:) Recursively compare left subtrees AND right subtrees.
            return checker(p.left, q.left) and checker(p.right, q.right)

        # (step 5:) Start recursion from both roots and return the result.
        return checker(p, q)
    
solution = Solution()
print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))) # Output: True
print(solution.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))) # Output: False
print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2)))) # Output: False

# Time Complexity: O(n), where n is the number of nodes in the trees.
# Space Complexity: O(h), where h is the height of the trees due to recursion stack.