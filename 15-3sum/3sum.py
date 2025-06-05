class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1 

            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum == -nums[i] :
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and  nums[r] == nums[r+1]:
                        r -= 1
                elif two_sum < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return ans
