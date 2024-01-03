from collections import Counter
class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bit_set = ["0"] * size
        self.bit_set_2 = ["1"] * size
        self.ct = 0
    
    def fix(self, idx: int) -> None:
        if self.bit_set[idx] == "0":
            self.bit_set[idx] = "1"
            self.bit_set_2[idx] = "0"
            self.ct += 1

    def unfix(self, idx: int) -> None:
        if self.bit_set[idx] == "1":
            self.bit_set[idx] = "0"
            self.bit_set_2[idx] = "1"
            self.ct -= 1

    def flip(self) -> None:
        self.bit_set_2 , self.bit_set = self.bit_set, self.bit_set_2 
        self.ct = self.size - self.ct
        
    def all(self) -> bool:
        return self.ct == self.size

    def one(self) -> bool:
        return self.ct > 0

    def count(self) -> int:
        # print(self.ct)
        return self.ct
        

    def toString(self) -> str:
        return ''.join(self.bit_set)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()