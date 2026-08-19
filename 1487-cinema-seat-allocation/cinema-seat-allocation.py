class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dct = defaultdict(list)

        for i, j in reservedSeats:
            dct[i].append(j)
        res = 0

        for key, values in dct.items():
            v1, v2, v3 = 1, 1, 1
            for value in values:
                if 2 <= value <= 5:
                    v1 = 0
                if 4 <= value <= 7:
                    v2 = 0
                if 6 <= value <= 9:
                    v3 = 0
            res += (max(v2, v1+v3))
        res += ((n - len(dct)) * 2)
        return res
                