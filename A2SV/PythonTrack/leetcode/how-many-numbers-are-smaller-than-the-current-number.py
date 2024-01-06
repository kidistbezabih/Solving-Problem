class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = []
        for i in range(n):
            minCount = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    minCount += 1
            l.append(minCount)
        return l