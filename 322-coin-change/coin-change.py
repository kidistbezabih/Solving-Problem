class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dp(amount, i):
            if i == n or amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            return min(dp(amount - coins[i], i) + 1, dp(amount, i+1))
        
        ans = dp(amount, 0)
        return ans if ans != float('inf') else -1
            
