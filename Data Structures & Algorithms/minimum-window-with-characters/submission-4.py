class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nt = {}
        for i in range(len(t)):
            nt[t[i]] = 1 + nt.get(t[i],0)

        have, need = 0, len(nt)
        window = {}
        ans, l = '', float('infinity')
        i = 0
        for j in range(len(s)):
            window[s[j]] = 1 + window.get(s[j],0)
            if s[j] in nt and window[s[j]] == nt[s[j]]:
                have += 1
            while have == need:
                window[s[i]] -= 1
                if s[i] in nt and window[s[i]] < nt[s[i]]:
                    have -= 1
                if j - i < l:
                    l = j - i
                    ans = s[i:j+1]
                i += 1
        if have == need and len(s) - i -1 < l:
            ans = s[i:len(s)]
        return ans