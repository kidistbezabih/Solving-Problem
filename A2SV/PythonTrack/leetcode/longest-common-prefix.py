class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = min(len(s) for s in strs)
        f = strs[0]
        s= ""
        x = 0
        for i in range(mn):
            for j in range(len(strs)):
                if strs[j][i] != f[i]:
                    return f[:x]
            x+=1
                
        return f[:x]
