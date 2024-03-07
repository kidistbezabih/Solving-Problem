class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque(tickets)
        count = 0

        while q[k] > 0:
            s = q.popleft()
            q.append(s-1)
            k -=1
            
            if k < 0:
                k+=len(q)
            if s-1>=0:
                count += 1
        return count