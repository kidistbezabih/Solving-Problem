class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)-1                

        for i in range(r):
            for j in range(r-i):
                matrix[i][j], matrix[r-j][r-i] = matrix[r-j][r-i], matrix[i][j]


        matrix.reverse()

