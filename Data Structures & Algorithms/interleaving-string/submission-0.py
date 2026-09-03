class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        mem = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in mem:
                return mem[(i, j)]
            res = False
            # we check both cases incase both i, j are equal to the same i + j in s3
            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                res |= dfs(i, j + 1)
            mem[(i, j)] = res
            return res

        return dfs(0, 0)