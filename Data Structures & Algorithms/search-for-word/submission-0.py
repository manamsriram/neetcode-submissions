class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        path = set()
        # cur tracks the current character in the word we are searching for
        def rec(i, j, cur):
            if cur == len(word):
                return True
            if i >= r or j >= c or i < 0 or j < 0 or board[i][j] != word[cur] or (i,j) in path:
                return False
            path.add((i, j))
            res = (rec(i + 1, j, cur + 1) or 
            rec(i, j + 1, cur + 1) or 
            rec(i - 1, j, cur + 1) or 
            rec(i, j - 1, cur + 1))

            path.remove((i, j))
            return res
            
        for i in range(r):
            for j in range(c):
                if rec(i, j, 0):
                    return True
        return False