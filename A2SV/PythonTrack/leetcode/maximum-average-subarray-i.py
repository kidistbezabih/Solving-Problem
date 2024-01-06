class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        lis =  []
        for i in  range(k):
            sum += nums[i]
        average = sum/k
        lis.append(sum)
        for i in range(1, len(nums) - k+1):
            sum = sum - nums[i-1]   +  nums[k+i-1]
            if sum/k > average:
                average = sum/k
        return(float("{:.5f}".format(average)))
