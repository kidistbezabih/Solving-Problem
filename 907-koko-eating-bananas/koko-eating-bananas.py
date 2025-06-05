class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = right - (right-left)//2

            hours = 0

            for p in piles:
                hours += ceil(p/mid)
            
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left  