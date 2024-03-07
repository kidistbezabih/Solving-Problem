class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.person = [persons[0]]

        d= defaultdict(int)
        d[persons[0]] = 1
        _max , key = 1, self.persons[0]

        for i in range(1, len(persons)):
            d[persons[i]] += 1
            if d[persons[i]] >= _max:
                _max = d[persons[i]]
                key = persons[i]
                self.person.append(persons[i])
            else:
                self.person.append(key)


    def q(self, t: int) -> int:
        left = bisect_left(self.times, t)
        if left >= len(self.person) or self.times[left] > t:
            left -= 1
        return self.person[left]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)