class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * n
        for a,b in invocations:
            adj[a].append(b)
            indegree[b] += 1

        susp = set()
        def dfs(k):
            susp.add(k)

            for node in adj[k]:
                indegree[node] -= 1
                if not node in susp: 
                    dfs(node)

        dfs(k)

        for u, v in invocations:
            if u not in susp and v in susp:
                # We can't remove anything, return all methods
                return list(range(n))
                
        # 3. If it's safe to remove, return only the non-suspicious methods
        return [i for i in range(n) if i not in susp]