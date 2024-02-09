class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        p_sm = [0] * n
        for first,  last, seats in bookings:
            p_sm[first-1] += seats
            if last < n:
                p_sm[last] -= seats
        
        for i in range(1, n):
            p_sm[i] += p_sm[i-1]
        return p_sm