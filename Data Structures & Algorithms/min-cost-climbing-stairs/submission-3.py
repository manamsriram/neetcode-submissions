class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost1, cost2 = 0, cost[0]
        for i in range(2, len(cost) + 1):
            temp = cost2
            cost2 = cost[i - 1] + min(cost1, cost2)
            cost1 = temp
        return min(cost1, cost2)