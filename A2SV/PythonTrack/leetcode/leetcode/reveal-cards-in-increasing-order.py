class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        index = []
        ans = [0]*n
        q = deque([i for i in range(n)])

        while len(q) > 1:
            index.append(q.popleft())
            q.append(q.popleft())
        index.append(q.popleft())
        
        for i in range(n):
            ans[index[i]] = deck[i]
        return ans