class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}

        for i in range(len(s)):
            last_occurence[s[i]] = i

        anchor, j = 0, 0
        ans = []

        for i in range(len(s)):
            j = max(j, last_occurence[s[i]])
            if i == j:
                ans.append(j - anchor + 1)
                anchor = i+1
        return ans