class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        last = nums[-1]

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > last:
                left = mid+1
            elif nums[mid] < last:
                right = mid - 1
            else:
                return nums[left]
        return  nums[left]
