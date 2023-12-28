class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        answer = []
        for i in nums:
            if i > 0:
                positives.append(i)
            else:
                negatives.append(i)
        for i in range(len(nums)//2):
            answer.append(positives[i])
            answer.append(negatives[i])
        return answer