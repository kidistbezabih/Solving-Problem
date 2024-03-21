class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5:0, 10:0, 20:0}

        for coin_value in bills:
            if coin_value == 5:
                count[5] += 1
            elif coin_value == 10:
                if count[5] >= 1:
                    count[5] -= 1
                    count[10] += 1
                else:
                    return False
            else:
                if count[10] >= 1:
                    count[10] -= 1
                    if count[5] >= 1:
                        count[5] -= 1
                    else:
                        return False
                else:
                    if count[5] >= 3:
                        count[5] -= 3
                    else:
                        return False
                count[coin_value] += 1
        return True


                