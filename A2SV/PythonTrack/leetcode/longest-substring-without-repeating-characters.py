class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        window = {}
        left  = right = 0
        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
                right += 1
            else:
                del window[s[left]]
                left += 1
            if len(window) > mx:
                mx = len(window)
        return mx
            