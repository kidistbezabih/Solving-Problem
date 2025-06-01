class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        cache = {}

        def dp(num):
            if num in cache:
                return cache[num]
            
            if num not in numSet:
                cache[num] = 0
                return cache[num]
            cache[num] = dp(num-1)+1
            return cache[num]
        if not nums:
            return 0
        for num in nums:
            dp(num)
        return max(cache.values())