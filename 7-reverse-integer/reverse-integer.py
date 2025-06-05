class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True

        x = abs(x)
        prev = 0
        while x:
            rem = x%10
            prev = prev*10 + rem
            x //= 10

        if neg:
            prev = -prev

        if -2**31 <= prev <= 2**31 - 1:
            return prev
        return 0
