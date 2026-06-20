class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # store indices
        l = 0
        ans = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Check if max index value if out of bounds
            if l > q[0]:
                q.popleft()
            if(r+1 >= k):
                ans.append(nums[q[0]])
                l += 1
        return ans