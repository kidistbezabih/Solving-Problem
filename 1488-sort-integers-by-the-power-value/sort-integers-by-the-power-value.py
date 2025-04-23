class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def dp(num):
            if num == 1:
                return 1
            if num in memo:
                return memo[num]
            if num % 2 == 0:
                memo[num] = ( 1 + dp(num // 2))
            else:
                memo[num] = (1 + dp(num*3 + 1))
            return memo[num]

        arr = []
        for i in range(lo, hi+1):
            arr.append((dp(i), i))
        arr.sort()
        return arr[k-1][1]