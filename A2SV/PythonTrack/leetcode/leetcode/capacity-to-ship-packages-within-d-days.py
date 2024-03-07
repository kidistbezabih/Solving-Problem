class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = left

        while left <= right:
            mid = left + (right - left)//2

            capacity = 0
            count = 0
            for i in range(len(weights)):
                if capacity + weights[i] <= mid:
                    capacity += weights[i]
                else:
                    count += 1
                    capacity = weights[i]
            
            if count < days:
                right = mid - 1
        
            else:
                left = mid + 1
        return left
                
