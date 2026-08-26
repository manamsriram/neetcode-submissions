class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        # stores number of ways to get to an amount from 0 to amount using 0 to index coins
        memo = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # number of ways to get amount of 0
        for i in range(len(coins) + 1):
            memo[i][0] = 1

        # pass index of current coin and current target amount
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                res = 0
                if a >= coins[i]:
                    # take this coin
                    res = memo[i][a - coins[i]]
                    # do not take this coin
                    res += memo[i + 1][a]
                memo[i][a] = res
        
        return memo[0][amount]