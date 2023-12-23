class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = ""
        d = []
        for i in range(len(s)):
            d.append((s[i] , indices[i]))
        d.sort(key =  lambda x : x[1])
        # d = sorted(d.items(), key= operator.itemgetter(1))
        for i in d:
            st += i[0]
        return(st)