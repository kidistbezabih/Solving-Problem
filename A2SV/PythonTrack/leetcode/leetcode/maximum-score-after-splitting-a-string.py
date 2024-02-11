class Solution(object):
    def maxScore(self, s):
        ln = len(s)
        ones = s.count('1')
        zeros = 0
        res = 0
        for i in range(ln-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            res = (max(res, ones+zeros))
        return res
        # length = len(s)
        # ones = 0
        # tmpScore = 1 if s[0] == '0' else 0
        # score = tmpScore
        
        # for i in range(1, length - 1):
        #     if s[i] == '0':
        #         tmpScore += 1
        #     else:
        #         ones += 1
        #         tmpScore -= 1

        #     if tmpScore > score:
        #         score = tmpScore
        
        # ones += 1 if s[length - 1] == '1' else 0

        # return ones + score
        