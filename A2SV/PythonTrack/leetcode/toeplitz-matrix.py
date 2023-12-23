class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        flag = True
        x, y = 0, 0
        n = len(matrix)
        m = len(matrix[0])
        while x<n:
            initial = matrix[x][y]
            a, b = x, y
            while a<n and b<m:
                if initial != matrix[a][b]:
                    return False
                a+=1
                b+=1
            x+=1
        x, y = 0, 0
        while y<m:
            initial = matrix[x][y]
            c, d = x, y
            while c<n and d<m:
                if initial != matrix[c][d]:
                    return False
                c+=1
                d+=1
            y+=1

        return True
