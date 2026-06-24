# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # declares global varibale
        self.dfs(root)
        return self.res

    # dfs always finds the height or depth
    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left) # gives the height of the left subtree
        right = self.dfs(node.right) # gives the height of the right subtree
        
        self.res = max(self.res, left + right) # we add max heights from left and right subtree, which form a connection through the current root node

        return 1 + max(left, right) 
