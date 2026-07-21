class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rs, cs = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rs or c >= cs or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for i in range(rs):
            for j in range(cs):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j), ans)
        return ans