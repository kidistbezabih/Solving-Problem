class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        most_left, most_right= -1, -1
        if not nums:
            return [-1, -1]
        if nums[0] > target or nums[len(nums)-1] < target:
            return [-1, -1]
        
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid - 1
            if nums[left] == target:
                most_left = left

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[right] == target:
                most_right = right
        
        return [most_left, most_right]

