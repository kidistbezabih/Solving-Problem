class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = ""
        x = 0
        for i in spaces:
            new_s += s[x:i]+ " "
            x = i
        new_s += s[x:]
        return new_s