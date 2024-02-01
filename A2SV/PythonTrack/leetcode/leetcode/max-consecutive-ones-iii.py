class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        count , res= 0, 0

        while j < len(nums):
            if nums[j] == 0:
                count += 1
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i+=1

            res =max(res, (j-i)+1)
            j+=1
        return res