class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        st = ""
        while i < len(s):
            if i + 2 < len(s):
                if s[i+2] == "#":
                    st += chr(96+int(s[i:i+2]))
                    i+=3
                else:
                    st += chr(96+int(s[i]))
                    i+=1
            else:
                st += chr(96+int(s[i]))
                i+=1
        return st