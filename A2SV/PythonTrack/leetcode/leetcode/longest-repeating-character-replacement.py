class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n =len(s)
        d = defaultdict(int)
        res = 0
        i, j = 0, 0

        while j < n:
            d[s[j]] += 1
            if d and (j-i+1) - max(d.values()) > k:
                d[s[i]] -=1
                i+=1
            res = max(res, j-i+1)
            j+=1
        return res