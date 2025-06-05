class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclideanDistance(x,y):
            return ((x)**2 + (y)**2)

        heap = []
        for x, y in points:
            dist = -euclideanDistance(x, y)

            if len(heap) < k:
                heappush(heap, (dist, [x, y]))
            else:
                mn = heap[0][0]
                if dist > mn:
                    heappop(heap)
                    heappush(heap, (dist, [x, y]))
        ans = []
        while heap:
            dist, point = heappop(heap)
            ans.append(point)
        return ans

