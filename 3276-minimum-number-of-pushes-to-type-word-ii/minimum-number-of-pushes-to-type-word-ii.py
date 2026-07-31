class Solution:
    def minimumPushes(self, word: str) -> int:
        letterCount = Counter(word)
        heap = [-freq for freq in letterCount.values()]
        heapq.heapify(heap)   
        res = 0
        count = 0

        while heap:
            nxt = -heapq.heappop(heap)
            res += (((count // 8)+1) * nxt)
            count += 1
        return res