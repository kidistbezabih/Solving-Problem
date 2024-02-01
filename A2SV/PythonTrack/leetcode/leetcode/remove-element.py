class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j, count = 0 , 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                count += 1
            j+=1
        return count
                