class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mx = float("inf")
        ind = []
        answer = []
        for i in range(len(list1)):
           for j in range(len(list2)):
               if list1[i] == list2[j]:
                   if i+j <= mx:
                       mx = i+j
                       ind.append([list1[i], mx])
        for i in ind:
            if i[1] == mx:
                answer.append(i[0])
        return(answer)

        