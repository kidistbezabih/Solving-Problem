class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        mid = []
        greater = []
        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                less.append(i)
                
        return less+mid+greater
