class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_dist = 0
        for i in range(len(points)-1):
            
            if max_dist <  (points[i+1][0] - points[i][0]):
                max_dist =  points[i+1][0] - points[i][0] 
        return max_dist