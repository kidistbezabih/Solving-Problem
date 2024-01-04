class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ln = len(digits)
        val = 0
        for i in range(ln):
            val += 10**(ln-1-i) * digits[i]
        val += 1
        return(list(map(int, str(val))))
        