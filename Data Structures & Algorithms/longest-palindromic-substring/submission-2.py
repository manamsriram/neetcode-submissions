class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def helper(l, r):
            res = ''
            while l >= 0 and r < n and s[l] == s[r]:
                res = s[l:r + 1]
                l -= 1
                r += 1
            return res
        ans = '' 
        for i in range(n):
            odd = helper(i, i)
            eve = helper(i, i + 1)
            if len(odd) > len(ans):
                ans = odd
            if len(eve) > len(ans):
                ans = eve

        return ans