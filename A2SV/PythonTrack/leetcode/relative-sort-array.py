class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        answer = []
        freq = Counter(arr1)

        for i in arr2:
            for j in range(freq[i]):
                answer.append(i)
            freq.pop(i)

        sorted_dict = {k: freq[k] for k in sorted(freq)}
        for i in sorted_dict:
            for j in range(sorted_dict[i]):
                answer.append(i)
                
        return answer