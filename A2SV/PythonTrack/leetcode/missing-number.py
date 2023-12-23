class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mx = max(nums)
        ln = len(nums)
        if ln == mx + 1:
            return (mx + 1)
        else:
            for i in range(ln):
                if i not in nums:
                    return (i)   