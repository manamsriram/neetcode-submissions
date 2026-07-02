class MedianFinder:

    def __init__(self):
        self.n = 0
        self.heap = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.heap, num) 
        print(self.n, self.heap)
        self.n += 1
        while math.ceil(self.n / 2) + 1 < len(self.heap):
            heapq.heappop(self.heap)

    def findMedian(self) -> float:
        ans = float(0)
        x = heapq.heappop(self.heap)
        if self.n & 1 == 0:
            y = self.heap[0]
            ans = (x + y) / 2
        else:
            if self.n > 1:
                ans = float(self.heap[0])
            else:
                ans = float(x)
        heapq.heappush(self.heap, x)
        return ans