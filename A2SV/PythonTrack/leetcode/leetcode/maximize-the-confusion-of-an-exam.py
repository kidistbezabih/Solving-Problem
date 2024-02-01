class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        j , i = 0, 0
        trues , falses = 0, 0
        res = 0
        while j < len(answerKey):
            if answerKey[j] == 'T':
                trues += 1
            else:
                falses += 1
            while trues > k and falses > k:
                if answerKey[i] == 'T':
                    trues -= 1
                else:
                    falses -= 1
                i+=1
            res = max(res, j-i+1)
            j+=1
        return res