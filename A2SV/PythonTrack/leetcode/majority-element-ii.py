class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        number_frequency = Counter(nums)
        answer_list = []

        mode_frequency = len(nums)//3

        for i in number_frequency:
            if number_frequency[i] > mode_frequency:
                answer_list.append(i)
        return answer_list