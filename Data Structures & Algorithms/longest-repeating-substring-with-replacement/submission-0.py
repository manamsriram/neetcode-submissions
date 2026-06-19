class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        i = 0
        high, ans = 0, 0
        for j in range(len(s)):
            dict[s[j]] = 1 + dict.get(s[j], 0)
            high = max(high, dict[s[j]])
            length = j-i+1
            if (length - high) <= k:
                ans = max(ans, length)
            else:
                dict[s[i]]-=1
                i+=1
        return ans