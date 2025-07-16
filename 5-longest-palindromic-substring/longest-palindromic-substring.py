class Solution:
    def helper(self, left, right, s):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            word = self.helper(i, i, s)
            if len(word) > len(res):
                res = word

            word = self.helper(i, i+1, s)
            if len(word) > len(res):
                res = word
        return res