class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # maps chars to their bigger lexicographical char
        # we want to have empty lists for each char that can occur
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLen = min(len(word1), len(word2))
            # if sorted in lexicographical order and prefixes match the shorter word comes before longer word
            # if we see arm and arms, arm should come before arms and not the other way
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visited = {} # True if in current path and False if already visited and not in current path, if no entry then not visited yet

        ans = []
        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            ans.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        ans.reverse()
        return "".join(ans)