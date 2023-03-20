class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lenLis = len(nums)
        ind = []
        nums = sorted(nums)
        for i in range(lenLis):
            if nums[i] == target:
                ind.append(i)
        return ind

