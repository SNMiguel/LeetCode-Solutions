# LeetCode problem N101: Symmetric Tree
# Difficulty: Easy

from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Step 1: Check if the root is None
        if not root:
            return True
        
        # Step 2: Check if the root is a leaf node
        else:
            
            # Step 3: Define a recursive function to check symmetry
            def checker(t1, t2):
                
                # Step 3.1: Check if both nodes are None, return True
                if not t1 and not t2:
                    return True
                
                # Step 3.2: Check if one of the nodes is None, return False
                if not t1 or not t2:
                    return False
                
                # Step 3.3: Check if the values of both nodes are equal and recurse on children
                return(t1.val == t2.val and checker(t1.right, t2.left) and checker(t1.left, t2.right))
            
            # Step 4: Call the checker function with left and right children of the root
            return checker(root.left, root.right)
        
from collections import deque

class SolutionBFS:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Step 1: Check if the root is None
        if not root:
            return True  
        
        # Step 2: Initialize a queue for BFS
        queue = deque()
        queue.append((root.left, root.right))
        
        # Step 3: Process the queue
        while queue:
            
            # Step 3.1: Dequeue a pair of nodes
            t1, t2 = queue.popleft()
            
            # Step 3.2: Check if both nodes are None, continue
            if not t1 and not t2:
                continue
            
            # Step 3.3: Check if one of the nodes is None, return False
            if not t1 or not t2:
                return False
            
            # Step 3.4: Check if the values of both nodes are equal
            if t1.val != t2.val:
                return False
            
            #Step 4: Enqueue mirror children
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        
        # Step 5: If all checks passed, return True
        return True
    
class SolutionDFS:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Step 1: Check if the root is None
        if not root:
            return True  # empty tree is symmetric

        # Step 2: Initialize a stack for DFS
        stack = [(root.left, root.right)]
        
        # Step 3: Process the stack
        while stack:
            
            # Step 3.1: Pop a pair of nodes from the stack
            t1, t2 = stack.pop()
            
            # Step 3.2: Check if both nodes are None, continue
            if not t1 and not t2:
                continue
            
            # Step 3.3: Check if one of the nodes is None, return False
            if not t1 or not t2:
                return False
            
            # Step 3.4: Check if the values of both nodes are equal
            if t1.val != t2.val:
                return False
            
            # Step 4: Push mirror pairs
            stack.append((t1.left, t2.right))
            stack.append((t1.right, t2.left))
        
        # Step 5: If all checks passed, return True
        return True

root = [1,2,2,null,3,null,3]
root1 = [1,2,2,3,4,4,3] 
sol = Solution()
sol_bfs = SolutionBFS()
sol_dfs = SolutionDFS()
print(sol.isSymmetric(root1))  # Output: True
print(sol_bfs.isSymmetric(root1))  # Output: True
print(sol_dfs.isSymmetric(root))  # Output: False