class RandomizedSet:

    def __init__(self):
        self.randomSet = []
        self.dct = {}
        self._index = 0

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.dct[val] = self._index
        self.randomSet.append(val)
        self._index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        idx = self.dct[val]
        print(idx)
        self.randomSet[idx], self.randomSet[-1] = self.randomSet[-1], self.randomSet[idx] 
        self.dct[self.randomSet[idx]] = idx
        removed = self.randomSet.pop()
        self.dct.pop(removed)
        self._index -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomSet)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()