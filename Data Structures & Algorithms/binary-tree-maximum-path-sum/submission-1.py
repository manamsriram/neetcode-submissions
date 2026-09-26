# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = root.val
        stack = [root]
        mp = {None: 0}

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftMax = max(mp[node.left], 0)
                rightMax = max(mp[node.right], 0)

                res = max(res, node.val + leftMax + rightMax)
                mp[node] = node.val + max(leftMax, rightMax)

        return res