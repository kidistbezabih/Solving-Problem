class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = []

        for key, val in freq.items():
            heappush(heap, (-val, key))

        ans = []
        
        while len(heap) > 1:
            a1, a2 = heappop(heap)
            b1, b2 = heappop(heap)

            ans.append(a2) 
            ans.append(b2)
            if a1+1 < 0:
                heappush(heap, (a1+1, a2))
            if b1+1 < 0:
                heappush(heap, (b1+1, b2))

        if heap:
            x, y = heappop(heap)
            if x < -1:
                return ""
            else:
                ans.append(y)
        return "".join(ans)