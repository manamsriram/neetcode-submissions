class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # maps chars to their bigger lexicographical char
        # we want to have empty lists for each char that can occur
        adj = {c: [] for w in words for c in w}
        # stores the number of edges towards a char, that means in order to print char2 we need to have printed char1 if char1 -> char2
        # so we check which character can be printed first without any char depending on it to be printed
        indegree = {c: 0 for c in adj}
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
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].append(word2[j])
                        indegree[word2[j]] += 1
                    break

        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

        ans = ''
        while q:
            char = q.popleft()
            ans += char
            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        print(ans)
        return ans if len(ans) == len(indegree) else ''