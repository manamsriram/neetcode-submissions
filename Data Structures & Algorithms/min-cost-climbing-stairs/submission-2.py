class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (len(cost) + 1)
        dp[1] = cost[0]
        for i in range(2, len(cost) + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n])