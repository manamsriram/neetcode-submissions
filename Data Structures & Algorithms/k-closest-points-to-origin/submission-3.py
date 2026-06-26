class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # push eucl and index
        for i in range(len(points)):
            heapq.heappush(heap, [math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), i])
        ans = []
        for i in range(k):
            ans.append(points[heapq.heappop(heap)[1]])
        return ans
        # def eucl(x1, x2):
        #     return math.sqrt(x1 ^ 2 + y1 ^ 2)