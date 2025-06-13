class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        matrix = [([0] * (n+1)) for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text2[i] == text1[j]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max( matrix[i+1][j], matrix[i][j+1])

        return matrix[0][0]