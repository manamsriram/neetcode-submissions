class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        ans=[0 for i in range(len(nums) - k + 1)]
        i = 0
        ans[i] = -heap[0][0]
        for j in range(k,len(nums)):
            while heap and heap[0][1] <= i:
                heapq.heappop(heap)
            heapq.heappush(heap,(-nums[j],j))
            i += 1
            ans[i] = -heap[0][0]
        return ans