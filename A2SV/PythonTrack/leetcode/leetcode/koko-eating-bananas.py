class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        n = len(piles)
        best = right
        
        while left  <= right:
            mid = left +(right - left)//2
            time = 0
            for i in range(n):
                time += ceil(piles[i]/mid)
            if time <= h:
                right = mid-1
                best = mid
            else:
                left = mid + 1
                
        return best
