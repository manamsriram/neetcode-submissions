# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cur = k
        self.ans = 0
        self.dfs(root)
        return self.ans
        
    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.cur -= 1
        if self.cur == 0:
            self.ans = root.val
        self.dfs(root.right)