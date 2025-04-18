class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        res = []
        n = len(nums)

        def backtrack(i):
            if i == n:
                return

            for j in range(i, len(nums)):
                res.append(nums[j])
                ans.append(res[:])

                backtrack(j+1)
                res.pop()
        backtrack(0)
        return ans