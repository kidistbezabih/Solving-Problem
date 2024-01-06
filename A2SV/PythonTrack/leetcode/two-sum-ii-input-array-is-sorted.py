class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) -1
        k = 0
        for i in range(len(numbers)):
            if numbers[k] + numbers[j] > target:
                j -= 1
            elif numbers[k] + numbers[j] < target:
                k += 1
            else:
                return ([k+1, j+1])
                break

