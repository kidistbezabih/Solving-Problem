class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]
        _min = float("inf")
        result = float("-inf")
        n = len(nums)
        flag = False

        for i in range(n):
            prefix.append(nums[i] + prefix[-1])
            if nums[i] >= 0:
                flag = True
        if flag:
            for i in range(len(prefix)):
                _min = min(_min, prefix[i])
                result = max(result, (prefix[i] - _min))
            return result
        else:
            return max(nums)