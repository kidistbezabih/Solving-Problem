class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newLis = []
        for i in range(n):
            newLis.append(nums[i])
            newLis.append(nums[n+i])
        return(newLis)