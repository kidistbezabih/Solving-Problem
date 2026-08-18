class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        count = [0] * 51
        res = 0

        for num in nums:
            count[num] += 1
        if k == 1:
            for i in range(50, -1, -1):
                if count[i] == 1:
                    return i
        else:
            if count[nums[0]] == 1 and count[nums[n-1]] == 1:
                return max(nums[0], nums[n-1])
            elif count[nums[n-1]] == 1:
                return nums[n-1]
            elif count[nums[0]] == 1:
                return nums[0]
        return -1
                


        



