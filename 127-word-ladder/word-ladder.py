class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbor = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbor[pattern].append(word)

        res = 1
        queue = deque([beginWord])
        visited = set([beginWord])
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for w in neighbor[pattern]:
                        if w not in visited:
                            queue.append(w)
                            visited.add(w)
            res += 1
        return 0