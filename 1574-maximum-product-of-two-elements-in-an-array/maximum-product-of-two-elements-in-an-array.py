class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0
        n = len(nums)

        for i in range(n):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif (nums[i] > second):
                second = nums[i]
        return (first - 1) * (second - 1) 