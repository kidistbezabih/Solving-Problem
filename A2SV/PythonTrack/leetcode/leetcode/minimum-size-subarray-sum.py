class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        i, j = 0, 0
        sm = 0
        while j < len(nums):
            sm += nums[j]
            if sm >= target:
                while sm >= target:
                    sm -= nums[i]
                    res = min(res, j-i+1)
                    i+=1    
            j+=1
        if res == float('inf'):
            return 0
        return res