class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)

        for key, val in counter.items():
            heappush(heap, (val, key))


        while len(counter) - k > 0:
            heappop(heap)
            k+=1

        ans = []

        for i, j in heap:
            ans.append(j)

        return(ans)