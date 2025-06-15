class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        ans = []
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                ans.append(" ".join(res))
                return

            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    res.append(s[i:j+1][:])
                    backtrack(j+1)
                    res.pop()
        backtrack(0)
        return ans