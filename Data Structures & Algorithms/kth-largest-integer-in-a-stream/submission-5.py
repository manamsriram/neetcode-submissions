class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.n = k
        heapq.heapify(self.heap)
        for i in nums:
            heapq.heappush(self.heap, i)
        for i in range(len(nums) - k):
            heapq.heappop(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.n:
            heapq.heappop(self.heap)
        return self.heap[0] if self.heap else val
