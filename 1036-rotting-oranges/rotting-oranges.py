class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        round = 0
        fresh = 0

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            flag = False
            for _ in range(len(queue)):
                row, col = queue.popleft()
                visited.add((row, col))

                for r,c in directions:
                    new_row,new_col = r+row, col+c
                    if not inbound(new_row, new_col):
                        continue
                    if grid[new_row][new_col] == 1:
                        flag = True

                    if inbound(new_row, new_col) and (new_row, new_col)not in visited and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            if flag:
                round += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1        
        return round