class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rs, cs = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rs or c >= cs or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(rs):
            for j in range(cs):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count