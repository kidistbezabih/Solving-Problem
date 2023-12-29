class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = sorted(nums)
        consecutives = []
        count = 1
        for i in range(len(x)-1):
            if(x[i + 1] - x[i] <= 1):
                if(x[i + 1] - x[i] == 1):
                    count += 1
                else:
                    pass
            else:
                consecutives.append(count)
                count = 1
            consecutives.append(count)
        if(len(x) > 1):
            return (max(consecutives))
        else: 
            if(len(x) == 1):
                return len(x)
            else:
                return 0