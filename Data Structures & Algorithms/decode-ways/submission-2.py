class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp, dp1, dp2
        # n -1, n, n + 1
        dp = 0
        dp1, dp2 = 1, 0

        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                dp = dp1

            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp += dp2
            
            # move left
            dp1, dp2 = dp, dp1
            dp = 0
        
        return dp1