class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minutes = 0

        while q and fresh > 0:
            minutes += 1
            l = len(q)
            # for every CURRENT rotten element check all four directions
            for k in range(l):
                i ,j = q.popleft()
                for dr, dc in directions:
                    row, col = i + dr, j + dc
                    if (row in range(0, r)) and (col in range(0, c)) and grid[row][col] == 1:
                        q.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1

        return minutes if fresh == 0 else -1