class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        def split(i):
            if i >= len(s):
                ans.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    split(j + 1)
                    part.pop()

        def isPalindrome(s, i, j):
            rev = s[i:j+1]
            rev = rev[::-1]
            return s[i:j+1] == rev
        split(0)
        return ans
            