class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @cache
        # def dp(amount):
        #     if amount < 0:
        #         return float('inf')
        #     if amount == 0:
        #         return 0
        #     ans = float('inf')
        #     for c in coins:
        #         ans = min(ans, 1 + dp(amount - c))
        #     return ans
        
        # ans = dp(amount)
        # return ans if ans != float('inf') else -1
        
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[-1] if dp[-1] != float('inf') else -1
