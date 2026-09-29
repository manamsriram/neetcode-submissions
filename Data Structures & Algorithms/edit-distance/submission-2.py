class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        # base case if one array is empty, then return the len of rest of the other array
        # dp[0][0] means taking all characters of both words and it stores minimum number of operations
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i

        for i in range(m - 1, -1 , -1):
            for j in range(n - 1, -1, -1):            
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # delete - (i + 1, j), insert - (i, j + 1)
                    # deleting from word1 will invalidate current i, some move i forward
                    # inserting will insert before the element, so i will still point to the same element. As we insert word2[j], we move j forward as both inserted and j are equal
                    # last is replace, to make both characters equal, so move both forward
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]
