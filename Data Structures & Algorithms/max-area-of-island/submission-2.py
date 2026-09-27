class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rs, cs = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            area = 1
            q = deque()
            q.append([r, c])
            while q:
                a, b = q.popleft()
                visit.add((a, b))
                for i, j in directions:
                    di, dj = a + i, b + j
                    if di < 0 or dj < 0 or di >= rs or dj >= cs or grid[di][dj] == 0 or (di, dj) in visit:
                        continue
                    q.append([di, dj])
                    visit.add((di, dj))
                    area += 1
            return area

        for i in range(rs):
            for j in range(cs):
                if grid[i][j] == 1 and (i, j) not in visit:
                    ans = max(dfs(i, j), ans)
        return ans