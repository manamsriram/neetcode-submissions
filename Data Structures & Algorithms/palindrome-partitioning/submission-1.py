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
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        split(0)
        return ans
            