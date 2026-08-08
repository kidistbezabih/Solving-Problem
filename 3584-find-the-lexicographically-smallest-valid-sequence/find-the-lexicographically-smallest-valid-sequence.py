class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        # finding the last occurence of character in word2

        n, m = len(word1), len(word2)
        last = [-1] * m
        j = m-1

        for i in range(n-1, -1, -1):
            if j < 0: break
            if word2[j] == word1[i]:
                last[j] = i
                j -= 1
        
        j = 0
        res = []
        chance = True
        for i in range(n):
            if j == m: break

            if word1[i] == word2[j]:
                res.append(i)
                j+=1

            elif chance and (j == m-1 or last[j+1] > i):
                res.append(i)
                j+=1
                chance = False

        return  [] if len(res) < m else res            

