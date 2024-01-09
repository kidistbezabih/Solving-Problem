class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        amount = 0
        for i in range(len(costs)):
            if (amount + costs[i]) > coins:
                break
            else:
                amount += costs[i] 
                count +=1
        return count