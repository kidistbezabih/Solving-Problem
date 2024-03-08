class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        new = [i for i in range(n) if s[i] == '1']
        ans = 0
        newlen = len(new)

        for i in range(newlen):
            ans += n - (newlen - i)-new[i]

        return ans