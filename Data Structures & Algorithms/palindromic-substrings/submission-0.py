class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def helper(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        ans = 0
        for i in range(n):
            ans += helper(i, i)
            ans += helper(i, i + 1)

        return ans