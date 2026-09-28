class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            res = 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            mem[(i, j)] = res
            return res
        return dfs(0, 0)
