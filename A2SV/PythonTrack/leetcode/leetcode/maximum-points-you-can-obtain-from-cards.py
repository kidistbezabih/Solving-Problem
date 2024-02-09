class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum  = sum(cardPoints)
        sm = sum(cardPoints[:len(cardPoints)-k])
        res = total_sum - sm 
        i, j = 0, len(cardPoints) - k

        while j<len(cardPoints):
            sm = sm - cardPoints[i] + cardPoints[j]
            res = max(res, total_sum - sm)
            i+=1
            j+=1
        return res
