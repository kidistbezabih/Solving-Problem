class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        k_count = nums.count(k)
        max_gain = 0

        for i in range(1, 51):
            if i == k:
                continue
            curr = max_curr = 0
            for num in nums:
                if num == k:
                    curr -= 1
                elif num == i:
                    curr += 1
                curr = max(curr, 0)
                max_curr = max(curr, max_curr)
            max_gain = max(max_gain, max_curr)
        return max_gain + k_count
