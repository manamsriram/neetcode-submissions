class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(s):
            if s == 0:
                return 0
            if s in dp:
                return dp[s]
            res = 1e9
            for coin in coins:
                if s - coin >= 0:
                    res = min(res, 1 + dfs(s - coin))
            dp[s] = res
            return res

        ans = dfs(amount)
        return -1 if ans >= 1e9 else ans
