class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ln = len(nums)
        ls = []
        count = 0
        for i in range(ln):
            if nums[i] == 1:
                count += 1
            else:
                ls.append(count)
                count = 0
            ls.append(count)
        return(max(ls))