# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # returns (best_path_in_subtree, best_downward_path_from_node)
        def dfs(node):
            if not node:
                # For an empty node, subtree max is -inf (invalid),
                # downward path is 0 (contributes nothing).
                return float('-inf'), 0

            leftBest, leftDown = dfs(node.left)
            rightBest, rightDown = dfs(node.right)

            # clamp negative downward paths to 0
            leftDown = max(leftDown, 0)
            rightDown = max(rightDown, 0)

            # best path that *passes through* this node (split)
            through = node.val + leftDown + rightDown

            # best path anywhere in this subtree
            bestSub = max(leftBest, rightBest, through)

            # best downward path starting at this node (no split)
            down = node.val + max(leftDown, rightDown)

            return bestSub, down

        best = dfs(root)
        return best[0]