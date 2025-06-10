class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        
        for i in range(m):
            for j in range(n):

                if i+j == 0:
                    dp[(i, j)] = 1
                else:
                    ne = [(i-1, j), (i, j-1)]
                    steps = 0
                    for a in ne:
                        if 0 <= a[0] < m and 0 <= a[1] < n:
                            steps += dp[a]
                    dp[(i, j)] = steps 
        return dp[m-1, n-1]