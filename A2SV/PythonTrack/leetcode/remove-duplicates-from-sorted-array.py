class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        count  = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
                count +=1
        return count
        
        