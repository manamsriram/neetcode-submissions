# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(root, m):
            if root is None:
                return 0
            ans = 0
            if root.val >= m:
                ans = 1
            m = max(root.val, m)
            ans += dfs(root.left, m)
            ans += dfs(root.right, m)
            return ans
        return dfs(root, root.val)
