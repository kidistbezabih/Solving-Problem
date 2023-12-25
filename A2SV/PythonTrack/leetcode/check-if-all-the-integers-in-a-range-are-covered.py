class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s1 = set()
        s2 = set()
        for i in ranges:
            for j in range(i[0], i[1]+1):
                s1.add(j)
        for i in range(left, right+1):
            s2.add(i)
        return (s2<=s1)
        # s1.add({i for i in ranges)