class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference_sort = sorted(costs, key = lambda  x:(x[0] - x[1]))
        ln = len(costs)
        i ,res = 0, 0

        while i < ln:
            if i < ln//2:
                res += (difference_sort[i][0])
            else:
                res += difference_sort[i][1]
            i+=1
        return res