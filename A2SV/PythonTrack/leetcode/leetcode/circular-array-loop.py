class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
        #     start = i
        #     j = nums[i]
        #     count = 1
        #     valid = True
        #     while j%len(nums) != start:
        #         if (j > 0 and nums[i] < 0) or (j < 0 and nums[i] > 0) or count >= len(nums):
        #             valid = False
        #             break
        #         j+=nums[j%len(nums)]
        #         j = j%len(nums)
        #         count += 1
                
        #     if valid and count > 1 and j%len(nums) == start:
        #         return True
        # return False

            start = i
            j = start + nums[i]
            count = {start}

            while j%len(nums) != start:
                if (nums[j%len(nums)] > 0 and nums[i] < 0) or (nums[j%len(nums)] < 0 and nums[i] > 0):
                    break
                if j in count:
                    break
                count.add(j)
                j+=nums[j%len(nums)]
                j = j%len(nums)
                
            if len(count) > 1 and j%len(nums) == start:
                return True
        return False
                
