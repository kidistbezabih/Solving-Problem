class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev_number = nums[-1]
        number_of_operations= 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= prev_number:
                prev_number = nums[i]
                continue
            
            x =  ceil(nums[i]/prev_number)
            number_of_operations += x - 1

            prev_number = nums[i] // x
        return number_of_operations

        