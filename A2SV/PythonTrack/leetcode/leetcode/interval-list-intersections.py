class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        answer = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] >= secondList[j][0]:
                if firstList[i][0] <= secondList[j][1]:
                    answer.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]) 
            if min(firstList[i][1], secondList[j][1]) == secondList[j][1]:
                j+=1
            else: i+=1
        return answer