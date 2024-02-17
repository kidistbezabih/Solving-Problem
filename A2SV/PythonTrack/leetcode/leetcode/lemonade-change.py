class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {
            "fives" : 0,
            "tens" : 0,
            "twenties" : 0
        }

        for i in bills:
            if i == 5:
                count["fives"] += 1
            elif i == 10 and count["fives"]:
                count["tens"] += 1
                count["fives"] -= 1
            elif i == 20 and count["tens"] and count["fives"]:
                count["tens"] -= 1
                count["fives"] -= 1
            elif i == 20 and count["fives"] >=3:
                count["fives"] -= 3
            else:
                return False
        return True