class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        heap = [[grid[0][0], 0, 0]] # max time encountered, row, col
        visit = set()
        visit.add((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while heap:
            time, row, col = heapq.heappop(heap)

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                neir, neic = row + dr, col + dc
                if neir < 0 or neic < 0 or neir == n or neic == n or (neir, neic) in visit:
                    continue
                visit.add((neir, neic))
                heapq.heappush(heap, [max(grid[neir][neic], time), neir, neic])

    