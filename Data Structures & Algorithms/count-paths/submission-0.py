class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in mem:
                return mem[(i, j)]
            mem[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return mem[(i, j)]
        return dfs(0, 0)