class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')
        i, j = 0, 0
        s = set()
        while j < len(cards):
            if cards[j] not in s:
                s.add(cards[j])
            else:
                while cards[i] != cards[j]:
                    s.remove(cards[i])
                    i+=1
                s.remove(cards[i])
                res = min(j-i+1, res)
                i+=1
                s.add(cards[j])
            j+=1
        if res == float('inf'):
            return -1          
        return res