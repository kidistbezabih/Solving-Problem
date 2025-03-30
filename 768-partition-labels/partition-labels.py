class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {}
        for i, c in enumerate(s):
            last_occ[c] = i

        ans, curr, last = [], 0, 0
        for i, c in enumerate(s):
            last = max(last, last_occ[c])
            
            if last_occ[c] == i and c == s[last]:
                ans.append(i+1-curr)
                curr = i+1
        return ans
