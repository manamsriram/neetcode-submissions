class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 == 1:
            return False
        target = total // 2

        dp = [[-1] * (target + 1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        
        def dfs(i, s):
            if target == 0:
                return True
            if s < 0 or i >= len(nums):
                return False
            if dp[i][s] != -1:
                return dp[i][s]
            dp[i][s] = dfs(i + 1, s) or dfs(i + 1, s - nums[i])
            return dp[i][s]

        return dfs(0, target)