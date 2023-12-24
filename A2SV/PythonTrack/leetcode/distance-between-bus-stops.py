class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = 0
        min_sum = 0
        if start > destination:
            start , destination = destination, start
        for i in range(len(distance)):
            total += distance[i]
            if i>= start and i < destination:
                min_sum += distance[i]

        return min(total- min_sum, min_sum)
