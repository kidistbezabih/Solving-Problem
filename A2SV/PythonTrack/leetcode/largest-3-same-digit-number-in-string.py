class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        mx = 0
        index = -1
        while i < len(num)-2:
            if len(set(num[i: i+3])) == 1:
                if mx <= int(num[i:i+3]):
                    mx = int(num[i:i+3])
                    index = i
            i+=1
        if index >= 0:
            return (num[index:index+3])
        return ''



            