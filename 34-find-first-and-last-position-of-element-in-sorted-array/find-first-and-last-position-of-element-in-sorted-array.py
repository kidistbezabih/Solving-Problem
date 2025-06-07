class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = right - (right-left)//2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        ans_left = left
        left, right = 0, len(nums)-1
        while left <= right:
            mid = right - (right-left)//2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        ans_right = right
        if not 0 <= ans_left < n or not 0 <= ans_right < n or nums[ans_right] != target:
            return [-1, -1]
        return [ans_left, ans_right]