class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        min_i = nums.index(min(nums))+1
        max_i = nums.index(max(nums))+1
        left = max(min_i, max_i)
        right = n - min(min_i, max_i)+1
        both = min(min_i, max_i) + n - max(min_i, max_i) + 1
        
        return min(left, right, both)
        
