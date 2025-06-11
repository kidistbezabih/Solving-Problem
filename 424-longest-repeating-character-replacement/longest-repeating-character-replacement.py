class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_count = {}
        ans = 0

        while r < len(s):
            if s[r] not in char_count:
                char_count[s[r]] = 0
            char_count[s[r]] += 1
            while r-l+1 - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    char_count.pop(s[l])
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans