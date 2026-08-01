class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def dp(l, r):
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            left = nums[l] - dp(l+1, r)
            right = nums[r] - dp(l, r-1)

            memo[l, r] = max(left, right)
            return memo[l, r]
        ans = dp(0, len(nums)-1)
        return True if ans >= 0 else False

