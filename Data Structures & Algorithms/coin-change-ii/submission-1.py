class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        # stores number of ways to get to an amount from 0 to amount using 0 to index coins
        memo = [[-1] * (amount + 1) for _ in range(amount + 1)]

        # pass index of current coin and current target amount
        def dfs(i, a):
            # number of ways to get amount of 0
            if a == 0:
                return 1
            # out of bounds
            if i >= len(coins):
                return 0
            if memo[i][a] != -1:
                return memo[i][a]
            res = 0
            if a >= coins[i]:
                # take this coin
                res = dfs(i, a - coins[i])
                # do not take this coin
                res += dfs(i + 1, a)
            memo[i][a] = res
            return res
        
        return dfs(0, amount)