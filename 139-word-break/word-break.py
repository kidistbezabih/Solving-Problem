class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}

        def dp(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i] 

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and dp(j):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return False

        return dp(0)


            