class Solution:
    def totalMoney(self, n: int) -> int:
        tot = 0
        amount = 0
        for i in range(n):
            if i % 7 == 0:
                amount = i // 7 + 1
            else:
                amount += 1
            tot += amount
        return tot