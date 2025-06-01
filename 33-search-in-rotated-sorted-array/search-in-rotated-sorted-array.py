class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findIndex(left, right):
            while left <= right:
                mid = left + (right - left)//2

                if nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        n = len(nums)
        left, right = 0, n - 1
        pivot = findIndex(left, right)

        if nums[pivot] <= target <= nums[-1]:
            left, right = pivot, n-1
        else:
            left, right = 0, pivot
            

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

        