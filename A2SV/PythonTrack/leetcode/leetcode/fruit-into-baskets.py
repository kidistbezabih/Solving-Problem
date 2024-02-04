class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        i, j = 0, 0
        d = defaultdict(int)

        while j < len(fruits):
            d[fruits[j]]+=1
            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    d.pop(fruits[i])
                i+=1
            j+=1
            res = max(res, j-i)
        return res