class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ln1 = len(word1)
        ln2 = len(word2)
        rem= ""
        if ln1 >= ln2:
            rem = word1
        else:
            rem = word2

        newstr =  ''
        for i in range(min(ln1, ln2)):
            newstr += word1[i]
            newstr += word2[i]
        return (newstr + (rem[min(ln1, ln2):]))