class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        ln = len(nums)
        lis = [0] * ln
        for req in requests:
            lis[req[0]] += 1
            if (req[1]+1) < ln:
                lis[req[1] + 1]-=1

        for i in range(1,ln):
            lis[i] += lis[i-1] 
        nums.sort()
        lis.sort()

        res = 0
        for i in range(ln):
            res += lis[i] *nums[i]
        return res % mod