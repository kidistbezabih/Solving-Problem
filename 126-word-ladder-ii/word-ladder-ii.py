from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = set(wordList)  # Make lookup faster
        neighbor = defaultdict(list)
        
        # Step 1: Build pattern-to-words map
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbor[pattern].append(word)

        # Step 2: BFS to find shortest paths and build graph
        parents = defaultdict(set)  # key: word, value: set of parents
        visited = set()
        found = False
        queue = deque([beginWord])
        visited.add(beginWord)
        
        while queue and not found:
            current_level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in neighbor[pattern]:
                        if nei not in visited:
                            if nei == endWord:
                                found = True
                            if nei not in current_level_visited:
                                queue.append(nei)
                                current_level_visited.add(nei)
                            parents[nei].add(word)
            visited.update(current_level_visited)

        # Step 3: Backtrack to build all paths from endWord to beginWord
        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                dfs(parent, path + [parent])

        if found:
            dfs(endWord, [endWord])
        return res
