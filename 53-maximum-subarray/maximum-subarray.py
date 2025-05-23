class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        max_running_sum = nums[0]

        for num in nums[1:]:
            running_sum = max(running_sum + num,  num)
            
            max_running_sum  = max(max_running_sum , running_sum)
        return max_running_sum 
