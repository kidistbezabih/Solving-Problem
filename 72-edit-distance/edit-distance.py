class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        cache = [[float('inf') for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            cache[i][n] = m-i
        for i in range(n+1):
            cache[m][i] = n-i


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[j] == word2[i]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])

        return cache[0][0] 


