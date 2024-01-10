class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = defaultdict(list)
        ans = []

        for i in points:
            d[i[0]**2 + i[1]**2].append(i)
            
        l = sorted(d.keys())
        i = 0
        count = k

        while count > 0:
            ans.extend(d[l[i]])
            count -= len(d[l[i]])
            i+=1
        return ans