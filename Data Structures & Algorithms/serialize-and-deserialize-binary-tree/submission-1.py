# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        # preorder traversal to map root, left, and right
        def dfs(node):
            if node is None:
                s.append('N')
                return
            s.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # ',' is because we want to preserve values like 10, 11
        # if not separator 11 will be '1','1' instead
        return ','.join(s)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == 'N':
                i += 1
                return None
            root = TreeNode(int(vals[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()