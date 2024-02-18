class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0

        for i in range(maxDoubles):
            if target == 1:
                break
            temp = target//2
            count += (target - (temp*2))+1
            target = temp
        count = (count + target-1)
        return count
