class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        subsum = 0
        ps = [0]
        length = len(nums)
        i , j = 0, 0
        s = set()

        for k in nums:
            ps.append(ps[-1] + k)
        
        while j < length:
            if nums[j] in s:
                subsum = max(ps[j]-ps[i], subsum)
                while nums[j] != nums[i]:
                    s.remove(nums[i])
                    i+=1
                i+=1
            else:
                s.add(nums[j])
            j+=1
        subsum = max(ps[j]-ps[i], subsum)
        return subsum