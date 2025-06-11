class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atla, pac = set(), set()

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols 
        
        def dfs(r, c, visited, prevHeight):
            if not inbound(r, c) or (prevHeight > heights[r][c]) or (r, c) in visited :
                return
            visited.add((r, c))
            neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for i, j in neigh:
                dfs(r+i, c+j, visited, heights[r][c])                


        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atla, heights[i][cols-1])
        
        for i in range(cols):
            dfs(0, i, pac, heights[0][i])
            dfs(rows-1, i, atla, heights[rows-1][i])

        ans = []
        for i in pac:
            if i in atla:
                ans.append(i)

        return ans