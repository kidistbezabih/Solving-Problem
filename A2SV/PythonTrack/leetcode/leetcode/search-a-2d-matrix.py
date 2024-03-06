class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lis = []
        for i in matrix:
            lis += i
        left , right = 0, len(lis)-1

        while left <= right:
            mid = left + (right - left)//2
            
            if lis[mid] > target:
                right = mid-1
            elif lis[mid] < target:
                left = mid + 1
            else:
                return True
        return False