class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ln = 0
        for i in trips:
            ln = max(ln, i[2])
        lis = [0] * (ln+1)

        for numPassanger, _from, _to in trips:
            lis[_from] += numPassanger
            if _to < len(lis):
                lis[_to] -= numPassanger
        if lis[0] > capacity:
            return False
        for i in range(1,len(lis)):
            lis[i] += lis[i-1]
            if lis[i] > capacity:
                return False
        return True
        