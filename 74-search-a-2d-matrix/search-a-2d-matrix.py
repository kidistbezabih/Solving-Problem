class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        best = -1

        while low <= high:
            mid = high - (high - low)//2
            if matrix[mid][0] <= target:
                low = mid + 1
                best = mid
            else:
                high = mid -1
        
        l, r = 0, len(matrix[0])-1
        low = best
        while l <= r:
            mid = r - (r - l)//2

            if matrix[low][mid] == target:
                return True
            elif matrix[low][mid] < target:
                l = mid +1
            else:
                r = mid - 1
        return False