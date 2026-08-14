class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top-down
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)