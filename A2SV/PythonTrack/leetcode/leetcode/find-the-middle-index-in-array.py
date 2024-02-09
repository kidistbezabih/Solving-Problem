class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lis = [0, nums[0]]
        if len(nums) == 1:
            return 0

        for i in range(1, len(nums)):
            lis.append(lis[-1]+nums[i])
        for i in range(1, len(lis)):
            if lis[-1] - lis[i] == lis[i-1]:
                return i-1
        return -1
