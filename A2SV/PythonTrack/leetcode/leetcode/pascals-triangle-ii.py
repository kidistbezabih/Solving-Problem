class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev= [1, 1]
        for i in range(rowIndex-1):
            new = [1]
            for j in range(1, len(prev)):
                new.append(prev[j] + prev[j-1])
            new.append(1)
            prev = new
        return prev
