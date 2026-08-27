class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        for i in range(n):
            for j in range(target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        return dp[n - 1][target]