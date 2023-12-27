class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        cp = capacity
        for i in range(len(plants)-1):
            cp -= plants[i]
            if cp < plants[i+1]:
                steps += 2*(i+1)
                cp = capacity
            steps += 1
        return steps