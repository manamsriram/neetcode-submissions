class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        # calculate adjacency list for every node as [distance, index]
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        visited = set()
        # stores cost and the index of point xi, yi
        heap = [[0, 0]]
        res = 0
        while len(visited) < n:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for nei in adj[node]:
                if nei[1] not in visited:
                    heapq.heappush(heap, nei)
        
        return res