class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            j = 0
            k = i-1
            
            while j < k :
                if nums[j] + nums[k] > nums[i]:
                    count += (k - j)
                    k-=1
                else:
                    j +=1
        return count