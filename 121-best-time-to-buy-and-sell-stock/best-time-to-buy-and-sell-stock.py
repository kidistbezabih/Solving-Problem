class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        l=0

        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            ans = max(ans, prices[r] - prices[l])

        return ans
            
            
