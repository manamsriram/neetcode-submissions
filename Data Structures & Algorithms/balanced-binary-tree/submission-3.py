# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.isbalanced = True
        height = self.dfs(root)
        return self.isbalanced

    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left) 
        right = self.dfs(node.right)
        if abs(left - right) > 1: # at each node, check if the subtree is imbalanced
            self.isbalanced = False
        return 1 + max(left, right)