class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            minutes += 1
            l = len(q)
            for k in range(l):
                point = q.popleft()
                i, j = point[0], point[1]
                if i + 1 < r and grid[i + 1][j] == 1:
                    q.append((i + 1, j))
                    grid[i + 1][j] = 2
                    fresh -= 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    q.append((i - 1, j))
                    grid[i - 1][j] = 2
                    fresh -= 1
                if j + 1 < c and grid[i][j + 1] == 1:
                    q.append((i, j + 1))
                    grid[i][j + 1] = 2
                    fresh -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    q.append((i, j - 1))
                    grid[i][j - 1] = 2
                    fresh -= 1

        return minutes if fresh == 0 else -1