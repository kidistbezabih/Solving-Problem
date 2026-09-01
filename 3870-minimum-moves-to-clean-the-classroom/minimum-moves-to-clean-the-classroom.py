import collections
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        if not classroom or not classroom[0]:
            return -1

        R, C = len(classroom), len(classroom[0])
        start_r, start_c = -1, -1
        total_litters = 0
        
        # 1. Find the Start position ('S') and count the total litter
        for r in range(R):
            for c in range(C):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    total_litters += 1
                    
        # 2. Set up our BFS Queue
        # The queue holds tuples of: (row, col, current_energy, collected_litter_set, steps_taken)
        # We use a `frozenset` to track collected litter so we don't double-count them
        queue = collections.deque([(start_r, start_c, energy, frozenset(), 0)])
        
        # 3. Visited Dictionary
        # We track the maximum energy we've had at any given state to prevent infinite loops.
        # A state is defined by: (row, col, which_litter_we_have_picked_up)
        visited = {}
        visited[(start_r, start_c, frozenset())] = energy
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c, e, collected, steps = queue.popleft()
            
            # Base case: If we have picked up all the litter, return the steps!
            if len(collected) == total_litters:
                return steps
            
            # If we are out of energy, we can't make any more moves from this cell
            if e == 0:
                continue
                
            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the next move is in bounds and NOT an obstacle
                if 0 <= nr < R and 0 <= nc < C and classroom[nr][nc] != 'X':
                    nxt_e = e - 1
                    nxt_collected = set(collected)
                    
                    # If it's litter, add its coordinates to our collected set
                    if classroom[nr][nc] == 'L':
                        nxt_collected.add((nr, nc))
                        
                    # If it's a recharge station, reset our energy
                    elif classroom[nr][nc] == 'R':
                        nxt_e = energy
                        
                    nxt_collected_frozen = frozenset(nxt_collected)
                    state = (nr, nc, nxt_collected_frozen)
                    
                    # Only add to queue if we haven't been in this state before, 
                    # OR if we are arriving here with MORE energy than we did last time
                    if state not in visited or visited[state] < nxt_e:
                        visited[state] = nxt_e
                        queue.append((nr, nc, nxt_e, nxt_collected_frozen, steps + 1))
                        
        # If the queue empties and we never found all the litter, it's impossible
        return -1