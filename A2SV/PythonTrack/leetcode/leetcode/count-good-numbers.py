class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        e = ceil(n/2)
        o = n //2
        res =(pow(5,e,mod)  * pow(4,o,mod))%mod
        return res