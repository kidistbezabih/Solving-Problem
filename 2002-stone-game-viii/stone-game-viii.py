class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + stones[i])
        dp = [0] * n
        dp[-1] = prefix[-1]

        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], prefix[i+1]-dp[i+1])
        return dp[1]
