class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        ones = 0
        best = ""
        
        for j in range(len(s)):
            # Expand the window
            if s[j] == '1':
                ones += 1
                
            # Shrink the window from the left IF:
            # 1. We have too many 1s.
            # 2. We have exactly k 1s, but there is a useless leading '0'.
            while ones > k or (ones == k and s[i] == '0'):
                if s[i] == '1':
                    ones -= 1
                i += 1
                
            # If our window is exactly valid, check if it beats our current best
            if ones == k:
                curr = s[i:j+1]
                if best == "":
                    best = curr
                elif len(curr) < len(best):
                    best = curr
                elif len(curr) == len(best):
                    best = min(best, curr) # min() handles lexicographical comparison naturally
                    
        return best