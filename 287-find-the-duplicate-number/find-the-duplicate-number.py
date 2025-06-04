class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            curr = abs(num)
            if nums[curr] < 0:
                return curr
            nums[curr] = -nums[curr]