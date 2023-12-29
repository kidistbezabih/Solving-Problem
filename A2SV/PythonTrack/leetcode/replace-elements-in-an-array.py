class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dictionary = {nums[i]:i for i in range(len(nums))}

        for i in operations:
            ind = nums_dictionary[i[0]] 
            nums[ind] = i[1]
            nums_dictionary[i[1]] = ind
            del(nums_dictionary[i[0]])

        return nums