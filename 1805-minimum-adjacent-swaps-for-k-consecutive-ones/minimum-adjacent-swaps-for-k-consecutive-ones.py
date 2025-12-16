class Solution:
    def minMoves(self, n: List[int], c: int) -> int:
        # Collect positions of all 1s
        pos = [i for i, v in enumerate(n) if v == 1]
        m = len(pos)

        # Edge cases
        if c <= 1:
            # If we need at most one 1, no swaps are necessary as long as a 1 exists.
            return 0 if m >= c else -1
        if m < c:
            # Not enough ones to ever get c consecutive ones
            return -1

        # Compressed positions to account for natural spacing when grouped
        compressed = [pos[k] - k for k in range(m)]

        # Prefix sums over compressed to allow O(1) window cost queries
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = pref[i] + compressed[i]

        best = float('inf')

        # Slide window of size c over the ones
        for i in range(m - c + 1):
            j = i + c - 1
            mid = (i + j) // 2
            median_val = compressed[mid]

            # cost to move all elements in window [i..j] to be consecutive
            # around the median position
            left_count = mid - i
            right_count = j - mid

            # Sum of distances on left side
            # median_val * left_count - sum(compressed[i:mid])
            left_cost = median_val * left_count - (pref[mid] - pref[i])

            # Sum of distances on right side
            # sum(compressed[mid+1:j+1]) - median_val * right_count
            right_cost = (pref[j + 1] - pref[mid + 1]) - median_val * right_count

            total_cost = left_cost + right_cost
            best = min(best, total_cost)

        return best if best != float('inf') else -1
