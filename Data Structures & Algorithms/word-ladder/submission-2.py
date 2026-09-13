class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        # every word is of same length
        m = len(wordList[0])
        
        wordSet = set(wordList)
        # contains all neighbors of a word after each pass
        qb, qe = deque([beginWord]), deque([endWord])
        # maps steps to reach a word from begin and end
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}
        
        while qb and qe:
            # always process the lesser length side
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                # for every index check all possible character replacements
                for j in range(m):
                    for c in range(ord('a'), ord('z') + 1):
                        pattern = word[:j] + chr(c) + word[j + 1:]
                        # base case where pattern does not match any word
                        if pattern not in wordSet:
                            continue
                        # the other side
                        if pattern in fromEnd:
                            return steps + fromEnd[pattern]
                        # the current side
                        if pattern not in fromBegin:
                            qb.append(pattern)
                            fromBegin[pattern] = steps + 1
                    
        return 0