class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        mem = {}
        def dfs(i, j):
            # base case if one array is empty, then return the len of rest of the other array
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in mem:
                return mem[(i, j)]
            if word1[i] == word2[j]:
                mem[(i, j)] = dfs(i + 1, j + 1)
            else:
                # delete - (i + 1, j), insert - (i, j + 1)
                # deleting from word1 will invalidate current i, some move i forward
                # inserting will insert before the element, so i will still point to the same element. As we insert word2[j], we move j forward as both inserted and j are equal
                mem[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1))
                # this is replace, to make both characters equal, so move both forward
                mem[(i, j)] = 1 + min(mem[(i, j)], dfs(i + 1, j + 1))
            return mem[(i, j)]

        return dfs(0, 0)
