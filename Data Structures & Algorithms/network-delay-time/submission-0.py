class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        heap = [(0, k)]
        visit = set()
        time = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            time = weight

            for nei, wei in edges[node]:
                if nei not in visit:
                    heapq.heappush(heap, (weight + wei, nei))

        return time if len(visit) == n else -1