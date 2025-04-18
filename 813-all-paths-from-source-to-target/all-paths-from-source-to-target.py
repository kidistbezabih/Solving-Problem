class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        res = [0]

        def backtrack(i):
            if i == len(graph) - 1:
                ans.append(res[:])
                return

            for node in graph[i]:
                res.append(node)

                backtrack(node)

                res.pop()
        backtrack(0)
        return ans