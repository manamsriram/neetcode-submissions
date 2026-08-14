class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True
        # bottom-up
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # check if the word from i to i + len(word)
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    # we mark the current substring as segmentable, if the other half of the segment is also segmentable
                    memo[i] = memo[i + len(word)]
                # if we already encounter a word that can be a part of the segement, we do not need to search the other words
                if memo[i]:
                    break

        return memo[0]