class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        while heap and len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            elif x > y:
                heapq.heappush(heap, -(x - y))
            else:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0