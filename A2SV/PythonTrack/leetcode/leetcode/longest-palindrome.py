class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        achieved = False
        max_len = 0
        for i in c:
            if c[i] % 2 == 0 or not achieved:
                max_len += c[i]
            else:
                max_len += c[i] - 1

            if c[i] % 2 == 1:
                achieved = True
        return max_len