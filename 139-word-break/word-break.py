class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {i:False for i in range(n+1)}
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n:
                    if w == s[i:i+len(w)] and dp[i+len(w)]:
                        dp[i] = dp[i+len(w)]
                        break
        return dp[0]
            