class Solution:
    def printVertically(self, s: str) -> List[str]:
        str_lis = s.split(" ")
        string = ""
        max_len = max([len(i) for i in str_lis])
        ans_lis = []
        for i in range(max_len):
            string = ""
            for j in range(len(str_lis)):
                if i >= len(str_lis[j]):
                    string += ' '
                else:
                    string += str_lis[j][i]
            ans_lis.append(string.rstrip())
        return ans_lis