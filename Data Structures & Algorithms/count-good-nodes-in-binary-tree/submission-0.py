# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, root.val)
        return self.ans
    
    def dfs(self, root, m):
        if root is None:
            return
        if root.val >= m:
            self.ans += 1
        m = max(root.val, m)
        self.dfs(root.left, m)
        self.dfs(root.right, m)
