class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        i = 0
        res = 0

        for j in range(n):
            if freq[nums[j]] == k:
                res = max(res, j-i)
                while nums[i] != nums[j]:
                    freq[nums[i]] -= 1
                    i += 1
                freq[nums[i]] -= 1
                i+=1
            freq[nums[j]] += 1
        res = max(res, j-i+1)
        return res
                
                
