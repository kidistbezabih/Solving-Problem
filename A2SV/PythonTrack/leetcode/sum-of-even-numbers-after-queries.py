class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        odd_sum , even_sum = 0, 0
        answer_lis = []

        for i in nums:
            if i %2 == 1:
                odd_sum += i
            else:
                even_sum += i

        for i in queries:
            if nums[i[1]] % 2 == 1:
                if i[0] % 2 == 1:
                    even_sum += (i[0] +nums[i[1]])
                    odd_sum -= nums[i[1]]
                else:
                    odd_sum += i[0]

            else:
                if i[0] % 2 == 1:
                    odd_sum += i[0] + nums[i[1]]
                    even_sum -= nums[i[1]]
                else:
                    even_sum += i[0]

            nums[i[1]] += i[0]
            answer_lis.append(even_sum)
            
        return answer_lis