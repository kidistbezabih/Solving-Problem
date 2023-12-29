# import
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = dict(Counter([i[0] for i in matches]).items())
        loosers = dict(Counter([i[1] for i in matches]).items())
        answer = [[], []]


        for i in winners:
            if i not in loosers:
                answer[0].append(i)

        for i in loosers:
            if loosers[i] < 2:
                answer[1].append(i)
        answer[0].sort()
        answer[1].sort()
        return answer 