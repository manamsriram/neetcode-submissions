# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, range):
            if root is None:
                return True
            if range[0] >= root.val or root.val >= range[1]:
                return False

            return dfs(root.left, [range[0], root.val]) and dfs(root.right, [root.val, range[1]])
        
        return dfs(root, [-float('inf'), float('inf')])