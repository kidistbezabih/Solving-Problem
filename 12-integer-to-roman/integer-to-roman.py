class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1000: "M",  
            900:"CM",
            500:"D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4:"IV",
            1: "I",
        }

        ans = ""

        while num:
            for n in d:
                if num >= n:
                    freq = num//n
                    ans += freq*d[n]
                    num -= (freq*n)
        return (ans)