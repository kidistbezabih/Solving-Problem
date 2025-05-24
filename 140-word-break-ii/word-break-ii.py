class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        res = []
        wordSet = set(wordDict)
        word = ""

        def backtrack(i):
            if i == len(s):
                ans.append(" ".join(res))
            
            for j in range(i, len(s)+1):
                if s[i:j] in wordSet:
                    res.append(s[i:j])
                    backtrack(j)
                    res.pop()
        backtrack(0)
        return ans
                