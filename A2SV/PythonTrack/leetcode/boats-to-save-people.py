class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats, i, j = 0, 0, len(people)-1
        people.sort()

        while i <= j:
            if people[i] + people[j] <= limit:
                i+=1
            j-=1
            boats += 1 
        return boats
        