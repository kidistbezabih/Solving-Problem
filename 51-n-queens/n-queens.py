class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        cols = set()
        negdig = set()
        posdig = set()

        board = [["."] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                ans = ["".join(row) for row in board]
                res.append(ans)
                return

            for c in range(n):
                if c in cols or r + c in negdig or r - c in posdig:
                    continue
                cols.add(c)
                negdig.add(r+c)
                posdig.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                negdig.remove(r+c)
                posdig.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
