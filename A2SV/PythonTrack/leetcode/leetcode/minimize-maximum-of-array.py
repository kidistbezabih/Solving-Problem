class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _max = nums[0]
        prefix = nums[0]

        for i in range(1, len(nums)):
            prefix += nums[i]

            if nums[i] > _max:
                _max = max(_max, math.ceil(prefix / (i + 1)))
                
        return _max