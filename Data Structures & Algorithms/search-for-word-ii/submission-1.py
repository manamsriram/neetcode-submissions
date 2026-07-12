class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, s):
        cur = self
        for c in s:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.addWord(word)
        
        rs, cs = len(board), len(board[0])
        res, visit = [], set()
        
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= rs or c >= cs or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end and word not in res:
                res.append(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(rs):
            for c in range(cs):
                dfs(r, c, root, '')

        return res
            