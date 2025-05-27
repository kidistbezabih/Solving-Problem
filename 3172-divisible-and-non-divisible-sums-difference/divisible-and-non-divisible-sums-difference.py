class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        tot = int(n*(n+1)/2)

        if m > n:
            return tot
        res, i = 0, m
        while i <= n:
            res  += i
            i += m
        return tot - res - res

            
        