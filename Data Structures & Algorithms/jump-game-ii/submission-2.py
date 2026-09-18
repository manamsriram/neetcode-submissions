class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1e9] * n
        dp[0] = 0
        for i in range(n):
            for j in range(nums[i]):
                end = i + j + 1
                if end < n:
                    dp[end] = min(dp[end], 1 + dp[i])
        return dp[n - 1]