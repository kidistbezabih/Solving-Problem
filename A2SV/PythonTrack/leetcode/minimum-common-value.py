class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0

        while nums1[i] !=nums2[j]:
            if nums1[i] > nums2[j]:
                j +=1
                if j >= len(nums2):
                    return -1
            if nums2[j] > nums1[i]:
                i +=1
                if i >= len(nums1):
                    return -1
        return nums1[i]