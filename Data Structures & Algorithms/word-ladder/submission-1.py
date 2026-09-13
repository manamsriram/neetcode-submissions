class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # N is number of words and M is length of each word
        # alternate would be: for every word check pattern matching by comapring every character of 2 words and then map word to word instead of pattern
        # but that would be N**2 * M
        # so we hack it to be N * M**2, where M is always smaller than N
        # maps patterns to words *oy -> [toy, joy]
        adj = collections.defaultdict(list)
        # add beginWord as it is also considered a node in the sequence
        wordList.append(beginWord)
        # for every word get pattern and append words to their lists
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        # regular bfs multi point search, like rotting oranges
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0