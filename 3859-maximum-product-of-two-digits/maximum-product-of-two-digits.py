class Solution:
    def maxProduct(self, n: int) -> int:
        first, second = 0, 0

        while (n > 0):
            r = n % 10
            if (r > first):
                second = first
                first = r
            elif (r > second):
                second = r

            n //= 10
            
        return first * second