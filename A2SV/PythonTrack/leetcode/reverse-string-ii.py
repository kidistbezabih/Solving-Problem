class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lis = []
        flag = True
        j = 0 
        for i in range(k, len(s), k):
            if flag:
                lis.append(s[i-k:i][::-1])
                flag = False
            else:
                lis.append(s[i-k:i])
                flag = True
            j =i
        if flag: 
            lis.append(s[j:len(s)][::-1])
        else:
            lis.append(s[j:len(s)])

        return "".join(lis)
