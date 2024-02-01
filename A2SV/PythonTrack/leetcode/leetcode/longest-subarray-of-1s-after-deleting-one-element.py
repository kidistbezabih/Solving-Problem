class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i , j = 0, 0
        res = 0
        count = 0
        while j < len(nums):
            if nums[j] == 0:
                count+=1
            while count > 1:
                if nums[i]== 0:
                    count-=1
                i+=1
            res = max(res, j-i)
            j+=1
        res = max(res,  j-i-1)
        return res



    # ### try
    #         i , j = 0, 0
    #     res = 0
    #     count = 0
    #     if nums[j] == 0:
    #         count += 1
    #     while j < len(nums):
    #         while count < 2:
    #             j+=1
    #             print(j)
    #             if nums[j] == 0:
    #                 count+=1
    #         res = max(res, j-i-1)
    #         while nums[i] != 0:
    #             i+=1
    #         count -= 1
    #         i+=1
    #         j+=1
    #     res = max(res,  j-i-1)
    #     return res
        #     while count < 2 and j < len(nums):
        #         if nums[j] == 0:
        #             count += 1
        #         j+=1
        #     res = max(res, j-i-1)
        #     # print('fd', res, i, j)
        #     i+=1
        #     while i < len(nums) and nums[i] != 0:
        #         print(i, nums[i], j)
        #         i+=1
        #     i+=1
        #     count -= 1
        # res = max(res, j - i-1)
        # print(res, i, j)
