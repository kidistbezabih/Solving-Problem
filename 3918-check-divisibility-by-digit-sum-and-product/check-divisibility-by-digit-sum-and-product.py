class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum, digitProduct = 0, 1
        orig = n

        while n:
            val = n%10
            digitSum += val
            digitProduct *= val
            n //= 10
        return orig % (digitProduct + digitSum) == 0

