class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        _max = max(nums)
        s = set(nums)
        ans = []

        for i in range(1, len(nums) + 1):
            if i not in s:
                ans.append(i)
        return ans
