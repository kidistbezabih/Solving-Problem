class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) -1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if order.index(words[i][j]) != order.index(words[i+1][j]):
                    if order.index(words[i][j]) > order.index(words[i+1][j]):
                        return False
                    break

        return True

            
