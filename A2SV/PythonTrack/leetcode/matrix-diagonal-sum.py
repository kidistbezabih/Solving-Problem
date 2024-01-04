class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)-1
        sm = 0
        for i in range(n+1):
            sm += mat[i][i]

        j = n
        for i in range(n+1):
            sm += mat[i][j-i]

        if (n +1) % 2 == 1:
            sm-=mat[len(mat)//2][len(mat)//2]
        return sm