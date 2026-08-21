class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visited = set()

        def bfs(i):
            q = deque()
            q.append(i)
            visited.add(i)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        component = 0
        for i in range(n):
            if i not in visited:
                component += 1
                bfs(i)

        return component