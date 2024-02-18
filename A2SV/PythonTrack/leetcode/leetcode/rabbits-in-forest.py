class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        res = 0

        for key, value in freq.items():
            res += (ceil(value/(key+1)) * (key + 1))
        return res

