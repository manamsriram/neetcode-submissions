class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        n = len(nums)
        # maps if we can reach target sum with nums from indices [0 ... i][target]
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                # we choose to skip the current number at nums[i - 1]
                dp[i][j] = dp[i - 1][j]
                # this is take choice if sum is less than or equal to target
                if nums[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]]

        return dp[n][target]