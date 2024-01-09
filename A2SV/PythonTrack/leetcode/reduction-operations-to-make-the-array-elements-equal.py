class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        ln = len(nums)

        for i in range(1, ln):
            if nums[i] != nums[i-1]:
                count += ln - i
        return count

        

        # def secondMax(lis, mx):
        #     s = float("-inf")
        #     ind = 0
        #     for i in range(len(lis)):
        #         if lis[i] > s and lis[i] < mx :
        #             # if lis
        #             s = lis[i]
        #             ind = i
        #     return ind

        # while len(set(nums)) > 1:
        #     f_max_ind = nums.index(max(nums))
        #     s_max_ind = secondMax(nums, nums[f_max_ind])
        #     diff = nums[f_max_ind] - nums[s_max_ind]
        #     nums[f_max_ind] -= diff
        #     count+=1

