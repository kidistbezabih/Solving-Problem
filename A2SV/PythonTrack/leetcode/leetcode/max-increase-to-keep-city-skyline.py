class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        transposed_grid = list(zip(*grid))
        mx_r =[0]*(n)
        mx_c =[0]*(n)
        res = 0

        for i in range(n):
            mx_r[i] = max(grid[i])
            mx_c[i] = max(transposed_grid[i])

        for i in range(n):
            for j in range(n):
                res += (min(mx_r[i], mx_c[j])- grid[i][j])

        return res
