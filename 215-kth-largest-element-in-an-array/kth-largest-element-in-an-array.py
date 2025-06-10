class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            if len(heap) < k:
                heappush(heap, nums[i])
            else:
                if heap[0] < nums[i]:
                    heappop(heap)
                    heappush(heap, nums[i])
        return heap[0] 