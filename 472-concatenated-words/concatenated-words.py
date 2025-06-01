class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        wordSet = set(words)
        dp = {}

        def findWord(word):
            if word in dp:
                return dp[word]

            for i in range(1,len(word)+1):
                prefix = word[:i]
                sufix = word[i:]
                
                if prefix in wordSet and (sufix in wordSet or findWord(sufix)):
                    dp[word] = True
                    return dp[word]
            dp[word] = False
            return dp[word]

        for word in words:
            if findWord(word):
                ans.append(word)
        return ans                    