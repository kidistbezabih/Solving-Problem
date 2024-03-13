class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        def hourGlassSum (grid, i, j):
            return sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])

        for i in range(1, n-1):
            for j in range(1, m-1):
                res =  max(res, hourGlassSum(grid, i, j))
        return res
            

