class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0]
        for i in nums:
            ans.append(i + ans[-1]) 
        return ans[1:]
