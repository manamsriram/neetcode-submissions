class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n - 1):
            if dp[i] == True:
                for j in range(nums[i]):
                    next = i + j + 1
                    if next < n:
                        dp[next] = True
        return dp[n - 1]