class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations, i, j = 0, 0, len(nums)-1
        nums.sort()

        while i<j:
            if nums[i] + nums[j] < k:
                i+=1
            elif nums[i] + nums[j] > k:
                j-=1
            else:
                i+=1
                j-=1
                operations += 1
        return operations