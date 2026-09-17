class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in mem:
                return mem[i]
            mem[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return mem[i]
        return min(dfs(0), dfs(1))