class RandomizedSet:

    def __init__(self):
        self.dct = {}
        self.random = []
        self.index = 0  

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.random.append(val)
        self.dct[val] = self.index
        self.index += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        ind = self.dct[val]
        self.random[self.index - 1], self.random[ind] = self.random[ind], self.random[self.index - 1]
        self.dct[self.random[ind]] = ind
        del self.dct[val]
        self.random.pop()
        self.index -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.random)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()