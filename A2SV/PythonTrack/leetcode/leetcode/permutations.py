class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def permutate(path, nums, index):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(len(nums)):
                path.append(nums[i])
                permutate(path, nums[:i] + nums[i+1:], index+1)
                path.pop()
        permutate([], nums, 0)
        return res
               