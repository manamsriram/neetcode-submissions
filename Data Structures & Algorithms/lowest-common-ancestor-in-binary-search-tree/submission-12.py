# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        fac = []
        while True:
            fac.append(cur)
            if cur.val == p.val:
                break
            elif p.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        cur = root
        i, ans = 0, fac[0]
        while True:
            if i < len(fac) and cur.val == fac[i].val:
                ans = fac[i]
                print(i, fac[i].val, ans.val)
            i += 1
            if cur.val == q.val:
                break
            elif q.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return ans
