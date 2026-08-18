class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distance = [100000000] * n
        visited = [False] * n
        edges = 0
        # current node index in points
        node = 0
        res = 0
        while edges < n - 1:
            visited[node] = True
            nextNode = -1
            for i in range(n):
                if visited[i]:
                    continue
                distance[i] = min(distance[i], (abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])))
                if nextNode == -1 or distance[i] < distance[nextNode]:
                    nextNode = i
            node = nextNode
            res += distance[nextNode]
            edges += 1

        return res