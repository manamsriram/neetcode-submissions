class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(amount + 1)] * (amount + 1)
        dp[0] = 0
        choice = [0] * (amount + 1)
        for a in range(1, amount + 1):
            res = (amount + 1)
            temp = 0
            for coin in coins:
                if a - coin >= 0:
                    if 1 + dp[a - coin] < res:
                        res = 1 + dp[a - coin]
                        temp = coin
            if res != (amount + 1):
                # get the best coin chosen here
                choice[a] = temp
            dp[a] = res
        if dp[amount] != (amount + 1):
            cur = amount
            path = []
            while cur != 0:
                path.append(choice[cur])
                cur -= choice[cur]
            print(path[::-1])
        return dp[amount] if dp[amount] != (amount + 1) else -1