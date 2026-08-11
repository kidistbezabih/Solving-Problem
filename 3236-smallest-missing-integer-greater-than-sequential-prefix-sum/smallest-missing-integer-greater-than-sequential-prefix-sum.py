class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        tot = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                tot += nums[i]
            else:
                break

        s = set(nums)

        while tot in s:
            tot += 1
        return tot