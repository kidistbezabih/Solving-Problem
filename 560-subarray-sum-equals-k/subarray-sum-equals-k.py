class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}
        curr_sum = 0 
        subarray_count = 0
        

        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_map:
                subarray_count += sum_map[curr_sum - k]
            if curr_sum not in sum_map:
                sum_map[curr_sum] = 0
            sum_map[curr_sum] += 1
        return subarray_count
