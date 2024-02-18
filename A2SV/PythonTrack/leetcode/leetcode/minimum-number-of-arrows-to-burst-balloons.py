class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()
        count = 1
        prev = points[0]

        for s, e in points[1:]:
            if s > prev[1]:
                count += 1
                prev = [s, e]
            else:
                prev[1] = min(prev[1], e)

        
        return count
            
