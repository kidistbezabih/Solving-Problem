class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        prefix_sum= [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
        
        for i in prefix_sum:
            d[i%k] += 1
            if d[i%k] > 1:
                count += d[i%k]-1

        return count