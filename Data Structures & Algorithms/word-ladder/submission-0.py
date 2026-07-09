class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                neighbors[pattern].append(word)
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[:j]+"*"+w[j+1:]
                    for m in neighbors[pattern]:
                        if m not in visited:
                            q.append(m)
                            visited.add(m)
            res+=1
        return 0