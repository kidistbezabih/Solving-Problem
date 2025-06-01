class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [0] * n

        for i in range(n-2, -1, -1):
            mn = float("inf")
            for j in range(i+1,min(n, i+nums[i]+1)):
                mn = min(steps[j], mn)
            steps[i] = mn+1
        return steps[0]
                

