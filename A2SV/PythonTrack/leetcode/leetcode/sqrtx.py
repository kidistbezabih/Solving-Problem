class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left)//2
            if mid*mid > x:
                right = mid-1
            elif mid * mid < x:
                left = mid+1
            else:
                return mid 
        return right