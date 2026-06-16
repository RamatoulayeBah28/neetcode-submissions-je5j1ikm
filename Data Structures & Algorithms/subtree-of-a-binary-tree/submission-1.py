# Understand 
# input a tree and a subtree
# output is a boolean true or false 
# if subtree is also in tree
# edge case: can we assume that both root and subroot are not empty? if they are what do we return?

# Match tree traversal using recursion (separate helper)
# 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1, 2, 3, 4, 5   # 2, 4, 5

class Solution:   
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False

        if self.sameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)   
        right = self.isSubtree(root.right, subRoot)
        return left or right
        
    def sameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None or root2 is None and root1 is not None:
            return False
        
        if root1.val != root2.val:
            return False

        left = self.sameTree(root1.left, root2.left)
        right = self.sameTree(root1.right, root2.right)
        return left and right

