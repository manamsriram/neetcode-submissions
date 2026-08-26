class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        # stores number of ways to get to an amount from 0 to amount using 0 to index coins
        memo = [0] * (amount + 1)
        # number of ways to get amount of 0
        memo[0] = 1

        # for a coin find number of ways to get this current sum from 1 to amount
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                if a >= coins[i]:
                    # take this coin and add it to count of number of ways when this coin is not taken
                    memo[a] += memo[a - coins[i]]
        
        return memo[amount]