class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return all(i%2 == 1 for i in nums1) or all(i%2 == 0 for i in nums1) or min(nums1)%2 == 1