class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # findign the product of the digit
        # fidng the reminder of the product divided by t
        #  return n + (t - reminder)

        def check(num) -> bool:
            pr = 1
            while num:
                pr *= (num % 10)
                num //= 10
            return pr%t == 0
        
         
        while not check(n):
            n+=1
        return n

