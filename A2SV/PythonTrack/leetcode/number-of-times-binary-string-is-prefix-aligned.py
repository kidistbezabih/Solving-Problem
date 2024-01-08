class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_index = 0

        for i in range(len(flips)):
            max_index = max(max_index, flips[i])
            if i+1 == max_index:
                count += 1
        return count
    
    
    
        # bit = [0]*len(flips)
        # prefix_alignes = 0
        # n = len(flips)
        # mx = 0

        # for i in range(n):
        #     bit[flips[i]-1] = 1
        #     if flips[i] > mx:
        #         mx = flips[i]
        #     if sum(bit) == mx:
        #         prefix_alignes += 1
        # return prefix_alignes
