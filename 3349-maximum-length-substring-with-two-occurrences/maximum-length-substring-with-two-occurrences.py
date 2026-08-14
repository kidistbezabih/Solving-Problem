class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        i, j = 0, 0
        n = len(s)
        res = 0

        while j < n:
            if count[s[j]] >= 2:
                res = max(res, j - i)
                while i < j and s[i] != s[j]:
                    count[s[i]] -= 1
                    i += 1
                count[s[i]] -= 1
                i +=1
            count[s[j]] += 1
            j+=1

        res = max(res, j - i)
        return res
            



        