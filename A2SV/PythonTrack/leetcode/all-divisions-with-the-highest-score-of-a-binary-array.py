class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0
        lis = [ones]

        for i in nums:
            if i == 0:
               zeros +=1
            else:
                ones -= 1
            lis.append(ones + zeros)
        mx = max(lis)
        return [i for i in range(len(lis)) if lis[i] == mx]
       
    