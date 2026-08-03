class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:    
        r, c = len(grid), len(grid[0])
        q = collections.deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i,j))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            l = len(q)
            # for every CURRENT element check all four directions
            for k in range(l):
                i ,j = q.popleft()
                for dr, dc in directions:
                    row, col = i + dr, j + dc
                    if (row in range(0, r)) and (col in range(0, c)) and grid[row][col] == 2**31 - 1:
                        q.append((row, col))
                        grid[row][col] = min(grid[i][j] + 1, grid[row][col])
