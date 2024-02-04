class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites, blacks = 0, 0
        res = float('inf')
        for i in (blocks[:k]):
            if i == 'W':
                whites += 1
        i, j = 0, k
        res = min(res, whites)
        while j < len(blocks):
            if blocks[i] == 'W':
                whites -= 1

            if blocks[j] == 'W':
                whites += 1
                
            res = min(res, whites)
            i+=1
            j+=1
        return res