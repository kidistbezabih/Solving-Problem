class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ln = len(s1)
        d_s1 = Counter(s1)
        d_s2 = Counter(s2[:len(s1)])
        i, j = 0, ln
        if d_s1 == d_s2:
            return True
        while j < len(s2):
            if d_s2[s2[i]] > 1:
                d_s2[s2[i]] -= 1
            else:
                d_s2.pop(s2[i])
            if  s2[j] in d_s2:
                d_s2[s2[j]] += 1
            else:
                d_s2[s2[j]] = 1
            if d_s1 == d_s2:
                return True
            i+=1
            j+=1
            print(d_s1, d_s2)
        return False


            