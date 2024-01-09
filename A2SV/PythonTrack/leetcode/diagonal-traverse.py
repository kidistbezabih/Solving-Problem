class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dic[i+j].append(mat[i][j])
        ls = []
        for k,v in dic.items():
            if k%2 == 0:
                ls.extend(reversed(v))
            else:
                ls.extend(v)
        return ls