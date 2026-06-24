# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.val == subRoot.val and self.sameTree(node, subRoot):
                return True
            stack.append(node.left)
            stack.append(node.right)
        return False

    def sameTree(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False
        
        return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)