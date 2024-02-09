class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p_s = [0]
        d = defaultdict(int)
        count = 0
        
        for i in nums:
            p_s.append(i+p_s[-1])
        for i in p_s:
            if i - k in d:
                count += d[i-k]
            d[i] += 1
        return count
