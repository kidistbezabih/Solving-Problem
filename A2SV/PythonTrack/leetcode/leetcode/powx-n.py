class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            if n % 2 == 1:
                n = (n-1)//2
                mul = self.myPow(x, n)
                return x * mul * mul
            mul = self.myPow(x, n//2)
            return mul * mul
        else:
            return 1 / self.myPow(x, abs(n))
        