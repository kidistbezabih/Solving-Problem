class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        flag = True
        dct = {
                "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
            }
        if len(s) > 1:
            for i in range(len(s)-1):
                if flag:
                    if dct[s[i+1]] > dct[s[i]]:
                        number += (dct[s[i+1]] - dct[s[i]])
                        flag = False
                    else:
                        number += dct[s[i]]
                else:
                    flag = True
        else:
            return dct[s[0]] 
        if dct[s[-2]] >= dct[s[-1]]:
            number += dct[s[-1]]
        return (number)

