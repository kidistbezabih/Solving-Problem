class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res = float('inf')
        n = len(nums)
        dct = defaultdict(int)
        dct[0] = -1
        tot = sum(nums)
        reminder = tot%p

        _sum = 0
        if reminder == 0:
            return 0
        for i in range(n+1):
            if (_sum - reminder) % p in dct:
                res = min(res, i - dct[(_sum - reminder) % p])
            dct[_sum%p] = i
            if i < n:
                _sum += nums[i]
            
        return res if res<len(nums) else -1