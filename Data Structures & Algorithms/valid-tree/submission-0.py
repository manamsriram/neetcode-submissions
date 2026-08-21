class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def bfs(node, par):
            q = deque()
            q.append([node, par])
            visited.add(node)
            while q:
                node, par = q.popleft()
                for nei in adj[node]:
                    if nei == par:
                        continue
                    if nei in visited:
                        return False
                    visited.add(nei)
                    q.append([nei, node])
            
            return True if len(visited) == n else False
        
        return bfs(0, -1)