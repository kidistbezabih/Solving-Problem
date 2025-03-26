from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr.extend(row)  # Flattens the grid into a 1D list

        arr.sort()
        median = arr[len(arr) // 2]  # Corrected median selection

        count = 0
        for num in arr:
            diff = abs(num - median)
            if diff % x != 0:
                return -1  # Impossible case
            count += diff // x  # Number of operations
        return count
