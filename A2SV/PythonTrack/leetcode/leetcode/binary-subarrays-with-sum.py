class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]
        d = defaultdict(int)
        count = 0

        for i in nums:
            prefix_sum.append(i+prefix_sum[-1]) 

        for i in prefix_sum:
            if i-goal in d:
                count += d[i-goal]
            d[i] +=1
        return count

