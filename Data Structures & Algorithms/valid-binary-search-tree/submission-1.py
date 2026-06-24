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
            # idea is when we go left, we need the value to be less than root, so max is the current root value
            # vice versa with right child, it should be greater than current root val, so min is root.val
            return dfs(root.left, [range[0], root.val]) and dfs(root.right, [root.val, range[1]])
        # root can be anywhere between -inf, to inf as there are no restrictions
        return dfs(root, [-float('inf'), float('inf')])