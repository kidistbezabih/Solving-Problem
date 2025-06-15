class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {i:False for i in range(n+1)}
        dp[n] = True
        wordDict = set(wordDict)
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = dp[j]
                    break
        return dp[0]
            